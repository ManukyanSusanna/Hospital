import csv
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

def execute_query(connection, table_name, query):
    connection.autocommit = False
    cursor = connection.cursor()
    try:
        with open(f"{table_name}_table.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                print(row)
                cursor.execute(query, row)

                connection.commit()
        print("The query was executed successfully")
    except OSError as e:
        print(f"The following error occurred:\n{e}")

insert_physician_table = """insert into physician(employee_id,name,position,ssn) 
                                    VALUES (%s , %s , %s , %s )"""

execute_query(connection, 'physician', insert_physician_table)

insert_department_table = "INSERT INTO department(department_id, name, head) VALUES (%s , %s , %s)"
execute_query(connection, 'department', insert_department_table) #change 1-2 d_name

insert_affiliated_with_table = "INSERT INTO affiliated_with(physician, department, primary_affiliation) VALUES (%s , %s , %s)"
execute_query(connection, 'affiliated_with', insert_affiliated_with_table)

insert_procedure_table = "INSERT INTO procedure(code, name, cost) VALUES (%s , %s , %s)"
execute_query(connection, 'procedure', insert_procedure_table)

insert_patient_table = "INSERT INTO patient(ssn, name, address, phone, insurance_id, pcp) VALUES (%s , %s , %s, %s , %s , %s)"
execute_query(connection, 'patient', insert_patient_table)

insert_trained_in_table = "INSERT INTO trained_in(physician, treatment, certification_date, certification_expires) VALUES (%s , %s , %s, %s)"
execute_query(connection, 'trained_in', insert_trained_in_table)

insert_nurse_table = "INSERT INTO nurse(employee_id, name, position, ssn) VALUES (%s , %s , %s, %s)"
execute_query(connection, 'nurse', insert_nurse_table)

insert_appointment_table = "INSERT INTO appointment(appointment_id, patient, prep_nurse, physician, start_time, end_time, examination_room) VALUES (%s , %s , %s, %s, %s , %s , %s)"
execute_query(connection, 'appointment', insert_appointment_table)

insert_medication_table = "INSERT INTO medication(code, name, brand, description) VALUES (%s , %s , %s, %s)"
execute_query(connection, 'medication', insert_medication_table)

insert_prescribes_table = "INSERT INTO prescribes(physician, patient, medication, date, appointment, dose) VALUES (%s , %s , %s, %s, %s, %s)"
execute_query(connection, 'prescribes', insert_prescribes_table)

insert_block_table = "INSERT INTO block(block_id, floor, code) VALUES (%s , %s , %s)"
execute_query(connection, 'block', insert_block_table)

insert_room_table = "INSERT INTO room(number, block_floor_code, unavailable) VALUES (%s , %s , %s)"
execute_query(connection, 'room', insert_room_table)

insert_on_call_table = "INSERT INTO on_call(nurse, block_floor_code, start_time, end_time) VALUES (%s , %s , %s, %s)"
execute_query(connection, 'on_call', insert_on_call_table)

insert_stay_table = "INSERT INTO stay(stay_id, patient, room, start_time, end_time) VALUES (%s , %s , %s, %s, %s)"
execute_query(connection, 'stay', insert_stay_table)

