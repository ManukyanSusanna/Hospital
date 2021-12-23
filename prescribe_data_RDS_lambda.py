import json
import psycopg2 as pg
from psycopg2 import OperationalError
import config
import generate_prescribe


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


def lambda_handler(event, context):
    # min_patientID = event['max_patient_id_before_insert']
    # max_patientID = event['max_patient_id_after_insert']
    min_patientID = 20
    max_patientID = 30

    insert_prescribes_table = """INSERT INTO prescribes(physician, patient, medication, date, appointment, dose) 
                                VALUES (%s , %s , %s, %s, %s, %s)"""

    execute_query_from_df(connection, generate_prescribe.df_creation(min_patientID, max_patientID),
                          insert_prescribes_table)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
min_patientID = 20
max_patientID = 30

insert_prescribes_table = """INSERT INTO prescribes(physician, patient, medication, date, appointment, dose) 
                                VALUES (%s , %s , %s, %s, %s, %s)"""

execute_query_from_df(connection, generate_prescribe.df_creation(min_patientID, max_patientID),
                          insert_prescribes_table)



