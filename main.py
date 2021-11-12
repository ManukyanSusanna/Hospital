import psycopg2 as pg
from psycopg2 import OperationalError


def create_connection(db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = pg.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Successfully connected to PostgreSQL DB")
    except OperationalError as e:
        print(f"The following error occures:\n{e}")
    return connection

connection = create_connection(
    db_user="postgres",
    db_password="Data2021",
    db_host='db-hospital.cednmbocimkf.eu-central-1.rds.amazonaws.com',
    db_port="5432"
)

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query was executed successfully!")
    except OperationalError as e:
        print(f"The foloowing error ocurred:\n{e}")

create_database_query = "CREATE DATABASE hospital_database"
#create_database(connection, create_database_query)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("The query was executed successfully")
    except OSError as e:
        print(f"The following error occurred:\n{e}")

create_physician_table = """
CREATE TABLE IF NOT EXISTS physician (
  employee_ID INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  position TEXT NOT NULL,
  ssn INTEGER NOT NULL
); 
"""

execute_query(connection, create_physician_table)

create_department_table = """
CREATE TABLE IF NOT EXISTS department (
  department_ID INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  head INTEGER REFERENCES physician(employee_ID)
);
"""

execute_query(connection, create_department_table)

create_affiliated_with_table = """
CREATE TABLE IF NOT EXISTS affiliated_with (
  physician INTEGER REFERENCES physician(employee_ID),
  department INTEGER REFERENCES department(department_ID),
  primary_affiliation BOOLEAN NOT NULL
);
"""

#The combination of physician, department will come once in that table.
execute_query(connection, create_affiliated_with_table)

create_procedure_table = """
CREATE TABLE IF NOT EXISTS procedure (
  code INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  cost REAL NOT NULL
);
"""

execute_query(connection, create_procedure_table)

create_trained_in_table = """
CREATE TABLE IF NOT EXISTS trained_in (
  physician INTEGER REFERENCES physician(employee_ID),
  treatment INTEGER REFERENCES procedure(code),
  certification_date TIMESTAMP NOT NULL,
  certification_expires TIMESTAMP NOT NULL
);
"""

execute_query(connection, create_trained_in_table)

create_patient_table = """
CREATE TABLE IF NOT EXISTS patient (
  ssn INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  address TEXT NOT NULL,
  phone TEXT NOT NULL,
  insurance_iD INTEGER NOT NULL,
  pcp INTEGER REFERENCES physician(employeeID)
);
"""

execute_query(connection, create_patient_table)

create_nurse_table = """
CREATE TABLE IF NOT EXISTS nurse (
  employee_ID INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  position TEXT NOT NULL,
  registered BOOLEAN NOT NULL,
  ssn INTEGER NOT NULL
);
"""

execute_query(connection, create_nurse_table)

create_appointment_table = """
CREATE TABLE IF NOT EXISTS appointment (
  appointment_iD INTEGER PRIMARY KEY NOT NULL,
  patient INTEGER REFERENCES patient(ssn),
  prep_nurse INTEGER REFERENCES nurse(employee_ID),
  physician INTEGER REFERENCES physician(employee_ID),
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP NOT NULL,
  examination_room TEXT NOT NULL
);
"""

#drop = "DROP TABLE appointment CASCADE"
#execute_query(connection, drop)
execute_query(connection, create_appointment_table)

create_medication_table = """
CREATE TABLE IF NOT EXISTS medication (
  code INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  brand TEXT NOT NULL,
  description TEXT NOT NULL
);
"""

execute_query(connection, create_medication_table)

create_prescribes_table = """
CREATE TABLE IF NOT EXISTS prescribes (
  physician INTEGER REFERENCES physician(employee_ID),
  patient INTEGER REFERENCES patient(ssn),
  medication INTEGER REFERENCES medication(code),
  date TIMESTAMP NOT NULL,
  appointment INTEGER REFERENCES appointment(appointment_ID),
  dose TEXT NOT NULL
);
"""

execute_query(connection, create_prescribes_table)

create_block_table = """
CREATE TABLE IF NOT EXISTS block (
  floor INTEGER NOT NULL,
  code INTEGER NOT NULL
); 
"""

execute_query(connection, create_block_table)


create_room_table = """
CREATE TABLE IF NOT EXISTS room (
  number INTEGER PRIMARY KEY NOT NULL,
  type TEXT NOT NULL,
  block_floor INTEGER NOT NULL,
  block_code INTEGER NOT NULL,
  unavailable BOOLEAN NOT NULL
);
"""

execute_query(connection, create_room_table)

create_on_call_table = """
CREATE TABLE IF NOT EXISTS on_call (
  nurse INTEGER REFERENCES nurse(employee_ID),
  block_floor INTEGER NOT NULL,
  block_code INTEGER NOT NULL,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP NOT NULL
);
"""
#PRIMARY KEY(Nurse, BlockFloor, BlockCode, Start, End),  FOREIGN KEY(BlockFloor, BlockCode) REFERENCES Block

execute_query(connection, create_on_call_table)

create_stay_table = """
CREATE TABLE IF NOT EXISTS stay (
  stay_ID INTEGER PRIMARY KEY NOT NULL,
  patient INTEGER REFERENCES patient(ssn),
  room INTEGER REFERENCES room(number),
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP NOT NULL
);
"""

execute_query(connection, create_stay_table)

create_transaction_table = """
CREATE TABLE IF NOT EXISTS transaction (
  patient INTEGER REFERENCES patient(ssn),
  procedure INTEGER REFERENCES procedure(code),
  stay INTEGER REFERENCES stay(stay_ID),
  date TIMESTAMP NOT NULL,
  physician INTEGER REFERENCES physician(employee_ID),
  assisting_nurse INTEGER REFERENCES nurse(employee_ID)
);
"""

#  PRIMARY KEY(Patient, Procedure, Stay, Date)

execute_query(connection, create_transaction_table)




