import json
import psycopg2 as pg
from psycopg2 import OperationalError
import boto3
import csv
import config

s3_client = boto3.client('s3')


def create_connection(db_user, db_password, db_host, db_port, db_name):
    connection = None
    try:
        connection = pg.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name
        )
        print("Successfully connected to PostgreSQL DB")
    except OperationalError as e:
        print(f"The following error occures:\n{e}")
    return connection


connection = create_connection(
    db_user=config.db_username,
    db_password=config.db_password,
    db_host=config.db_endpoint,
    db_port=config.db_port,
    db_name=config.db_name
)


def execute_query(connection, data, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        reader = csv.reader(data)
        next(reader)
        for row in reader:
            print(row)
            cursor.execute(query, row)

            connection.commit()
        print("The query was executed successfully")
    except OSError as e:
        print(f"The following error occurred:\n{e}")


def execute_select_max_query(connection, query):
    connection.autocommit = False
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            maximum = i[0]

        connection.commit()
        print("The query was executed successfully")
        return maximum
    except OSError as e:
        print(f"The following error occurred:\n{e}")


def lambda_handler(event, context):
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]
    print("bucket_name: ", bucket_name)
    print("Key ", s3_file_name)
    resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)

    select = "SELECT count(employee_id) from physician "

    data = resp['Body'].read().decode('utf-8')
    data = data.split("\n")

    insert_physician_table = """insert into physician(employee_id,name,position,ssn)
                                        VALUES (%s , %s , %s , %s )"""

    execute_query(connection, data, insert_physician_table)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
