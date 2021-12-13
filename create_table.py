import psycopg2 as pg
from psycopg2 import OperationalError
import config

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


# drop_physician = "DROP TABLE patient CASCADE"
# execute_query(connection, drop_physician)

# drop_department = "DROP TABLE department CASCADE"
# execute_query(connection, drop_department)
#
# drop_affiliated_with = "DROP TABLE affiliated_with CASCADE"
# execute_query(connection, drop_affiliated_with)
#
# drop_procedure = "DROP TABLE procedure CASCADE"
# execute_query(connection, drop_procedure)
#
# drop_trained_in = "DROP TABLE trained_in CASCADE"
# execute_query(connection, drop_trained_in)
#
# drop_patient = "DROP TABLE patient CASCADE"
# execute_query(connection, drop_patient)
#
# drop_nurse = "DROP TABLE nurse CASCADE"
# execute_query(connection, drop_nurse)
#
# drop_appointment = "DROP TABLE appointment CASCADE"
# execute_query(connection, drop_appointment)
#
# drop_medication = "DROP TABLE medication CASCADE"
# execute_query(connection, drop_medication)
#
# drop_prescribes = "DROP TABLE prescribes CASCADE"
# execute_query(connection, drop_prescribes)
#
# drop_block = "DROP TABLE block CASCADE"
# execute_query(connection, drop_block)
#
# drop_room = "DROP TABLE room CASCADE"
# execute_query(connection, drop_room)
#
drop_on_call = "DROP TABLE on_call CASCADE"
# execute_query(connection, drop_on_call)

# drop_stay = "DROP TABLE stay CASCADE"
# execute_query(connection, drop_stay)
#
# drop_undergoes = "DROP TABLE undergoes CASCADE"
# execute_query(connection, drop_undergoes)
#

execute_query(connection, read_content)


