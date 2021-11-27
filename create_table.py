import psycopg2 as pg
from psycopg2 import OperationalError


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
    db_user='postgres',
    db_password='postgres',
    db_host='localhost',
    db_port='5432',
    db_name='hospital_database'
)

file = open('create_table.txt', 'r')
read_content = file.read()

def execute_query(connection, query):
    connection.autocommit = False
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("The query was executed successfully")
    except OSError as e:
        print(f"The following error occurred:\n{e}")


# drop = "DROP TABLE appointment CASCADE"
# execute_query(connection, drop)

execute_query(connection, read_content)

