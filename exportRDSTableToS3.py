import json
import psycopg2 as pg
from psycopg2 import OperationalError
import boto3
import csv
import config
from io import StringIO
import sys
import tempfile
import fastparquet
import pandas as pd

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


def lambda_handler(event, context):
    bucket_name = "hosptalstaticcsv"
    s3_path = '/tmp/appointment.parquet'

    s3_resource = boto3.resource("s3")

    with tempfile.TemporaryFile() as tmpfile:
        stmt = 'appointment'
        copy_sql = "COPY appointment TO STDOUT WITH CSV HEADER"
        cursor = connection.cursor()
        cursor.copy_expert(copy_sql, tmpfile)
        tmpfile.seek(0)
        data_df = pd.read_csv(tmpfile)


    data_df.to_parquet(s3_path)
    s3_client.put_object(Bucket=bucket_name, Key=s3_path)
    df = pd.read_parquet(s3_path)
    print(df)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
