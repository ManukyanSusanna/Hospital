import string

import numpy as np
import pandas as pd
import random
import datetime
import csv
from faker import Faker

patient_count = 1000
physician_count = 100

class Patient:
    def __init__(self, ssn, name, address, phone, insurance_id, pcp):
        # self.id = id
        self.ssn = ssn
        self.name = name
        self.address = address
        self.phone = phone
        self.insurance_id = insurance_id
        self.pcp = pcp

    def __iter__(self):
        # yield self.id
        yield self.ssn
        yield self.name
        yield self.address
        yield self.phone
        yield self.insurance_id
        yield self.pcp


faker = Faker()
patients = []

for i in range(0,patient_count):
    # id = i + 1
    ssn = str(faker.random_int(100, 999)) + '-' + str(faker.random_int(10, 99)) + '-' +str(faker.random_int(1000, 9999))
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    insurance_id = faker.random.randint(100000, 999999)
    pcp = faker.random.randint(1, physician_count)
    patient = Patient(ssn, name, address, phone, insurance_id, pcp)

    patients.append(patient)

fields = ['ssn','name','address','phone','insurance_id','pcp']

filename = "patient_table.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    df_patient = pd.DataFrame(patients)
    df_patient.to_csv("patient_table.csv", index=False, header=fields)



#########################################################################################


# df = pd.read_csv("prescribes_table.csv")
# for _ in range(0,1000):
#     #df['physician'].values[random.sample(range(0, 1000), 100)] = random.randint(1, 100)
#     df.loc[random.sample(range(0, 1000), 100), 'physician'] = random.randint(1, 100)
#
#     df.loc[random.sample(range(0, 1000), 100), 'patient'] = random.sample(ssn_list, 100)
#     df.loc[random.randint(0, 1000), 'medication'] = random.randint(1, 200)
#     df.loc[random.randint(0, 1000), 'appointment'] = random.randint(1, 1000)
#     df.loc[random.randint(0, 1000), 'dose'] = random.randint(1, 100)
#
#     df.to_csv("prescribes_table.csv", index=False)
#
#
# df_stay = pd.read_csv("stay_table.csv")
# df_stay['end_time'] = df_stay['start_time'].apply(add_start_days)
#
# for _ in range(0,1000):
#     df_stay.loc[random.sample(range(0, 1000), 100), 'patient'] = random.sample(ssn_list, 100)
#     df_stay.loc[random.randint(0, 1000), 'room'] = random.randint(1, 250)
#
# df_stay.to_csv("stay_table.csv", index=False)
#
#
