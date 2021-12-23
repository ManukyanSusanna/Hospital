import json
import psycopg2 as pg
from psycopg2 import OperationalError
import config
import patient_generator
import boto3

client = boto3.client('lambda')


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


def execute_query_from_df(connection, df, query):
    connection.autocommit = True
    cursor = connection.cursor()
    print(df)
    try:
        for i in df.index:
            row = df.iloc[i].values.astype(str).tolist()
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


def execute_select_column_query(connection, query):
    connection.autocommit = False
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = [i[0] for i in cursor.fetchall()]
        connection.commit()
        print("The query was executed successfully")
        return result
    except OSError as e:
        print(f"The following error occurred:\n{e}")


def max_id_to_json(file_name, table_name, id_before_insert, id_after_insert):
    data = {}
    data[table_name] = []
    data[table_name].append({
        'max_id_before_insert': id_before_insert,
        'max_id_after_insert': id_after_insert,
    })

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


def lambda_handler(event, context):
    select_max_query = "Select MAX(patient_id) FROM patient"
    max_patient_id_before_insert = execute_select_max_query(connection, select_max_query)

    insert_patient_table = """INSERT INTO patient(patient_id, ssn, name, address, phone, insurance_id, pcp)
                                    VALUES (DEFAULT, %s, %s , %s, %s , %s , %s)"""

    execute_query_from_df(connection, patient_generator.df_patient, insert_patient_table)
    max_patient_id_after_insert = execute_select_max_query(connection, select_max_query)

    if (max_patient_id_before_insert == None):
        max_patient_id_before_insert = 0

    # max_id_to_json('utils.txt', 'patient', max_patient_id_before_insert, max_patient_id_after_insert)

    inputParams = {
        "max_patient_id_before_insert": max_patient_id_before_insert,
        "max_patient_id_after_insert": max_patient_id_after_insert
    }

    client.invoke(
        FunctionName='arn:aws:lambda:eu-central-1:923215935995:function:appointment_generator',
        InvocationType='RequestResponse',
        Payload=json.dumps(inputParams)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }