import string

import pandas as pd
import random
import datetime

df = pd.read_csv("patient_table.csv")
for _ in range(1,1000):
    df.loc[random.randint(0, 999), 'insurance_id'] = random.randint(100000, 999999)
    df.loc[random.randint(0, 99), 'pcp'] = random.randint(1, 101)

    df.to_csv("patient_table.csv", index=False)


def add_start_days(startdate) :
    end_date = pd.to_datetime(startdate) + pd.DateOffset(days=random.randint(1, 8))
    return end_date

# #print(add_start_days(startdate))
#
df_patient = pd.read_csv("patient_table.csv")
ssn_list = df_patient['ssn'].tolist()
#
df = pd.read_csv("appointment_table.csv")
#start_list = df['start_time'].tolist()
alphabet_list = string.ascii_uppercase

df['end_time'] = df['start_time'].apply(add_start_days)

for _ in range(0,1000):
    df.loc[random.randint(0, 999), 'prep_nurse'] = random.randint(1, 200)
    df.loc[random.randint(0, 999), 'physician'] = random.randint(1, 100)
    df.loc[random.sample(range(0, 1000), 1000), 'patient'] = random.sample(ssn_list, 1000)
    df.loc[random.randint(0, 999), 'examination_room'] = random.choice(alphabet_list)
    df.to_csv("appointment_table.csv", index=False)


df = pd.read_csv("prescribes_table.csv")
for _ in range(0,1000):
    #df['physician'].values[random.sample(range(0, 1000), 100)] = random.randint(1, 100)
    df.loc[random.sample(range(0, 1000), 100), 'physician'] = random.randint(1, 100)

    df.loc[random.sample(range(0, 1000), 100), 'patient'] = random.sample(ssn_list, 100)
    df.loc[random.randint(0, 1000), 'medication'] = random.randint(1, 200)
    df.loc[random.randint(0, 1000), 'appointment'] = random.randint(1, 1000)
    df.loc[random.randint(0, 1000), 'dose'] = random.randint(1, 100)

    df.to_csv("prescribes_table.csv", index=False)



