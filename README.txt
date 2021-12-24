3 problems that I come across in my project and solution



1.Event json content in lambda function

At first I uploud .csv file to S3 then I create lambda bunction, which upload csv data to RDS table. From S3 events I can't find event log. Then I change priority and first create lambda function and add trigger to S3 and get event


{
  "Records": [

    {

      "eventVersion": "2.1",

      "eventSource": "aws:s3",

      "awsRegion": "eu-central-1",

      "eventTime": "2021-12-09T13:26:12.425Z",

      "eventName": "ObjectCreated:Put",

      "userIdentity": {

        "principalId": "AF8HCWV4QVNA5"

      },

      "requestParameters": {

       "sourceIPAddress": "46.71.231.255"

      },

      "responseElements": {

        "x-amz-request-id": "50W50WR65284FZP6",

        "x-amz-id-2": "eyXGZMZqQA0fElRQJR+oQ9SBm5v12UfFseL+NgMJR5pZbNi3LslCjMPZh0OI58gJ/4N901Kdk5+pIS4eKsIjKEY8xN04HbgY"
      },

      "s3": {

        "s3SchemaVersion": "1.0",

        "configurationId": "S3ObjectsToRDS",

        "bucket": {

          "name": "hosptalstaticcsv",

          "ownerIdentity": {

            "principalId": "AF8HCWV4QVNA5"

          },

          "arn": "arn:aws:s3:::hosptalstaticcsv"

        },

        "object":

          {

            "key": "medication_table.csv",

            "size": 456,

            "eTag": "22d3c886fec26e40a7a73c2a265b850d",

            "sequencer": "0061B203F455CA956E"

          }

      }

    }

  ]

}
  

Then in code I can use

bucket_name = event["Records"][0]["s3"]["bucket"]["name"]

s3_medication_name = event["Records"][0]["s3"]["object"]["key"]

resp_medication = s3_client.get_object(Bucket=bucket_name, Key=s3_medication_name)


data_medication = resp_medication['Body'].read().decode('utf-8')

data_medication = data_medication.split("\n")
  


2.Calling an AWS Lambda function from another Lambda function

I have 'patient' table in which data is generated and depends on this patient-generated appointment, prescribes tables. I solve this problem by calling appointment, prescribes Lambda functions in patient Lambda function

In order to allow the patientFunction to call the appointmentFunction, I need to provide the patientFunction with specific rights to call another lambda function. This can be done by adding specific policies to a role and then assigning that role to the lambda function.
In the IAM module I added policy and in JSON file added 

"Action": [

                "lambda:InvokeFunction",

                "lambda:InvokeAsync"

            ],
"Resource": "arn:aws:lambda:eu-central-1:923215935995:function:appointment_generator"

Then I created role which I added to Lambda function configuration.
In patientFunction added

inputParams = {

        "max_patient_id_before_insert"   : max_patient_id_before_insert,

        "max_patient_id_after_insert"    : max_patient_id_after_insert

    }

client.invoke(

        FunctionName = 'arn:aws:lambda:eu-central-1:923215935995:function:appointment_generator',

        InvocationType = 'RequestResponse',

        Payload = json.dumps(inputParams)

    )


3. For export RDS table data to csv file I used 

query = "COPY appointment TO '/tmp/appointment.csv' WITH (FORMAT CSV, HEADER)"
    
 
cursor = connection.cursor()
   
cursor.execute(query)

One problem with running the COPY command as an postgres command is that I can only run it as superuser or my account needs to have the superuser privilege. I run this command as a regular user, and I got an error message like this:

ERROR: "must be superuser or a member of the pg_write_server_files role to COPY to a file\n
HINT:  Anyone can COPY to stdout or from stdin. psql's \\copy command also works for anyone.\n",

I changed query to
query = "COPY appointment TO STDOUT WITH CSV HEADER"

and get ERROR: "can't execute COPY TO: use the copy_to() method instead

I used instead of cursor.execute(query) 
cursor.copy_expert(query, tmpfile)

