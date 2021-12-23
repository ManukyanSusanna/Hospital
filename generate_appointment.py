import pandas as pd
import random
import string
from faker import Faker

nurse_count = 200
physician_count = 100


# df_patient = pd.read_csv("patient_table.csv")
# ssn_list = df_patient['ssn'].tolist()
# appointment_count = len(ssn_list)##

# import json
# min_patientID = None
# max_patientID = None
# with open('utils.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['patient']:
#         min_patientID = p['max_id_before_insert']
#         max_patientID = p['max_id_after_insert']

# df_nurse = pd.read_csv("nurse_table.csv")
# nurse_employee_id_list = df_patient['employee_id'].tolist()
# nurse_count = len(nurse_employee_id_list)


class Appointment:
    def __init__(self, appointment_id, prep_nurse, physician, start_time, end_time, examination_room):
        self.appointment_id = appointment_id
        self.prep_nurse = prep_nurse
        self.physician = physician
        self.start_time = start_time
        self.end_time = end_time
        self.examination_room = examination_room

    def __iter__(self):
        yield self.appointment_id
        yield self.prep_nurse
        yield self.physician
        yield self.start_time
        yield self.end_time
        yield self.examination_room


def add_start_days(startdate):
    end_date = pd.to_datetime(startdate) + pd.DateOffset(days=random.randint(1, 8))
    return end_date


faker = Faker()
alphabet_list = string.ascii_uppercase


def df_creation(min_patientID, max_patientID):
    appointments = []

    for i in range(min_patientID + 1, max_patientID + 1):
        # appointment_id = i + 1
        appointment_id = i
        prep_nurse = random.randint(1, nurse_count)
        physician = random.randint(1, physician_count)
        start_time = faker.date_time_between(start_date="-6y", end_date="now")
        end_time = add_start_days(start_time)
        examination_room = random.choice(alphabet_list)

        appointment = Appointment(appointment_id, prep_nurse, physician, start_time, end_time, examination_room)
        appointments.append(appointment)

    return pd.DataFrame(appointments)

# fields = ['appointment_id', 'patient', 'prep_nurse', 'physician', 'start_time', 'end_time', 'examination_room']
#
# filename = "appointment_table.csv"
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     df_appointment = pd.DataFrame(appointments)
#     df_appointment.to_csv("appointment_table.csv", index=False, header=fields)

