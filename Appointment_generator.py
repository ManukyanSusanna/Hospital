import faker.generator
import pandas as pd
import random
import datetime
import csv
import string
from faker import Faker

nurse_count = 200
physician_count = 100

# df_patient = pd.read_csv("patient_table.csv")
# ssn_list = df_patient['ssn'].tolist()
# appointment_count = len(ssn_list)##

import json

with open('utils.txt') as json_file:
    data = json.load(json_file)
    for p in data['patient']:
        ssn_list = p['ssn']
print(ssn_list)
appointment_count = len(ssn_list)
# df_nurse = pd.read_csv("nurse_table.csv")
# nurse_employee_id_list = df_patient['employee_id'].tolist()
# nurse_count = len(nurse_employee_id_list)


class Appointment:
    def __init__(self, appointment_id, patient, prep_nurse, physician, start_time, end_time, examination_room):

        self.appointment_id = appointment_id
        self.patient = patient
        self.prep_nurse = prep_nurse
        self.physician = physician
        self.start_time = start_time
        self.end_time = end_time
        self.examination_room = examination_room

    def __iter__(self):
        yield self.appointment_id
        yield self.patient
        yield self.prep_nurse
        yield self.physician
        yield self.start_time
        yield self.end_time
        yield self.examination_room

def add_start_days(startdate) :
    end_date = pd.to_datetime(startdate) + pd.DateOffset(days=random.randint(1, 8))
    return end_date


faker = Faker()
appointments = []
alphabet_list = string.ascii_uppercase

for i in range(0,appointment_count):
    appointment_id = i + 1
    patient = ssn_list[i]
    prep_nurse = random.randint(1, nurse_count)
    physician = random.randint(1, physician_count)
    start_time = faker.date_time_between(start_date = "-6y", end_date = "now")
    end_time = add_start_days(start_time)
    examination_room = random.choice(alphabet_list)

    appointment = Appointment(appointment_id, patient, prep_nurse, physician, start_time, end_time, examination_room)
    appointments.append(appointment)


fields = ['appointment_id', 'patient', 'prep_nurse', 'physician', 'start_time', 'end_time', 'examination_room']

filename = "appointment_table.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    df_patient = pd.DataFrame(appointments)
    df_patient.to_csv("appointment_table.csv", index=False, header=fields)

