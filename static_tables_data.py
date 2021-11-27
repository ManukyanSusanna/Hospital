import string

import pandas as pd
import random
import datetime

#reading the csv file
df = pd.read_csv("physician.csv")

# updating the column value/data

name = ['Anaesthetics', 'Cardiology', 'Dermatology', 'Emergency medicine', 'Neurology', 'Obstetrics and gynaecology', 'Ophthalmology', 'Paediatrics', 'Pathology', 'Psychiatry',
'Radiology', 'Surgery', 'Trauma and orthopaedics']
print('Your name is ' + random.choice(name) + '!')
for _ in range(1,100):
    df.loc[random.randint(0, 100), 'position'] = random.choice(name)
    df.to_csv("physician.csv", index=False)



df = pd.read_csv("affiliated_with_table.csv")
for _ in range(1,100):
    df.loc[random.randint(1, 100), 'physician'] = random.randint(1,100)
    df.loc[random.randint(1, 100), 'department'] = random.randint(1,11)
    df.loc[random.randint(0, 1), 'primary_affiliation'] = random.randint(0,1)

    df.to_csv("affiliated_with_table.csv", index=False)

df = pd.read_csv("procedure_table.csv")
name = ['Appendectomy', 'Cataract Surgery', 'C-Section', 'CT Scan', 'Echocardiogram', 'Heart Bypass Surgery',
        'Hip Replacement Surgery', 'MRI', 'Upper Endoscopy', 'X-Ray']

for i in range(0,10):
    df.loc[i, 'name'] = name[i]
    df.loc[i, 'cost'] = random.randint(5000, 25000)

    df.to_csv("procedure_table.csv", index=False)

df = pd.read_csv("trained_in_table.csv")
for _ in range(0,100):
    df.loc[random.sample(range(0, 100), 100), 'physician'] = random.sample(range(1, 101), 100)
    df.loc[random.randint(0, 99), 'treatment'] = random.randint(1, 10)

    df.to_csv("trained_in_table.csv", index=False)


df = pd.read_csv("nurse_table.csv")
name = ("Nursing assistant (CNA)", "Licensed practical nurse (LPN)", "Registered nurse (RN)", "Advanced practice registered nurses (APRNs)")
for _ in range(0,200):
    df.loc[random.randint(0, 199), 'position'] = random.choice(name)

    df.to_csv("nurse_table.csv", index=False)

df_exel = pd.read_excel('Medicines_output_herbal_medicines.xlsx', sheet_name='Worksheet 1')
namelist = df_exel['name'].tolist()
brandlist = df_exel['brand'].tolist()
uselist = df_exel['Use'].tolist()

df = pd.read_csv("medication_table.csv")
df['name'] = namelist
df['brand'] = brandlist
df['description'] = uselist

df.to_csv("medication_table.csv", index=False)


df = pd.read_csv("block_table.csv")

for i in range(0, 10):

    df['code'].values[i] = random.randint(10000, 99999)
    df.to_csv("block_table.csv", index=False)


df = pd.read_csv("room_table.csv")

for i in range(0,250):
    df['block_floor_code'].values[i] = random.randint(1, 10)

df.to_csv('room_table.csv', index=False)

def add_start_days(startdate) :
    end_date = pd.to_datetime(startdate) + pd.DateOffset(days=random.randint(1, 8))
    return end_date


df = pd.read_csv("on_call_table.csv")
df['end_time'] = df['start_time'].apply(add_start_days)

for i in range(0,200):
    df.loc[random.sample(range(0, 199), 100), 'nurse'] = random.sample(range(0, 200), 100)
    df['block_floor_code'].values[i] = random.randint(1, 10)

df.to_csv('on_call_table.csv', index=False)


df = pd.read_csv("stay_table.csv")
df['end_time'] = df['start_time'].apply(add_start_days)

for _ in range(0,1000):
    df.loc[random.sample(range(0, 1000), 100), 'patient'] = random.sample(ssn_list, 100)
    df.loc[random.randint(0, 1000), 'room'] = random.randint(1, 250)

df.to_csv("stay_table.csv", index=False)
