import boto3
from botocore.exceptions import NoCredentialsError
import config

ACCESS_KEY = config.ACCESS_KEY
SECRET_KEY = config.SECRET_KEY
location = config.location

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name = location
)

# # client.create_bucket(
# #     Bucket='hosptalstaticcsv',
# #     CreateBucketConfiguration=location
# # )
clientResponse = client.list_buckets()

print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

uploaded = upload_to_aws('physician_table.csv', 'hosptalstaticcsv', 'physician_table.parquet')
uploaded = upload_to_aws('physician_table.csv', 'hosptalstaticcsv', 'physician_table.csv')
uploaded = upload_to_aws('department_table.csv', 'hosptalstaticcsv', 'department_table.csv')
uploaded = upload_to_aws('procedure_table.csv', 'hosptalstaticcsv', 'procedure_table.csv')
uploaded = upload_to_aws('nurse_table.csv', 'hosptalstaticcsv', 'nurse_table.csv')
uploaded = upload_to_aws('trained_in_table.csv', 'hosptalstaticcsv', 'trained_in_table.csv')
uploaded = upload_to_aws('medication_table.csv', 'hosptalstaticcsv', 'medication_table.csv')
uploaded = upload_to_aws('affiliated_with_table.csv', 'hosptalstaticcsv', 'affiliated_with_table.csv')
uploaded = upload_to_aws('block_table.csv', 'hosptalstaticcsv', 'block_table.csv')
uploaded = upload_to_aws('room_table.csv', 'hosptalstaticcsv', 'room_table.csv')
uploaded = upload_to_aws('on_call_table.csv', 'hosptalstaticcsv', 'on_call_table.csv')
