import string

import pandas as pd
import random
import datetime

physician_count = 100
department_count = 11
procedure_count = 10
nurse_count = 200
block_count = 10
room_count = 250

df_physician = pd.read_csv("physician_table.csv")
physician_position_list = ['Anaesthetics', 'Cardiology', 'Dermatology', 'Emergency medicine', 'Neurology', 'Obstetrics and gynaecology',
                           'Ophthalmology', 'Paediatrics', 'Pathology', 'Psychiatry', 'Radiology', 'Surgery', 'Trauma and orthopaedics']
df_physician['id'] = df_physician['id'].astype(int)

for _ in range(0,physician_count):
    df_physician.loc[random.randint(0, physician_count - 1), 'position'] = random.choice(physician_position_list)
df_physician.to_csv("physician_table.csv", index=False)



df_affiliated = pd.read_csv("affiliated_with_table.csv")
for _ in range(0,physician_count):
    df_affiliated.loc[random.randint(0, physician_count - 1), 'physician'] = random.randint(1,physician_count)
    df_affiliated.loc[random.randint(0, physician_count - 1), 'department'] = random.randint(1,department_count)
    df_affiliated.loc[random.randint(0, 1), 'primary_affiliation'] = random.randint(0,1)

df_affiliated.to_csv("affiliated_with_table.csv", index=False)


df_procedure = pd.read_csv("procedure_table.csv")
procedure_name_list = ['Appendectomy', 'Cataract Surgery', 'C-Section', 'CT Scan', 'Echocardiogram',
        'Heart Bypass Surgery', 'Hip Replacement Surgery', 'MRI', 'Upper Endoscopy', 'X-Ray']

for i in range(0,procedure_count):
    df_procedure.loc[i, 'name'] = procedure_name_list[i]
    df_procedure.loc[i, 'cost'] = random.randint(5000, 25000)

df_procedure.to_csv("procedure_table.csv", index=False)


df_trained_in = pd.read_csv("trained_in_table.csv")
df_trained_in['treatment'] = df_trained_in['treatment'].astype(int)
for _ in range(0,physician_count):
    df_trained_in.loc[random.sample(range(0, physician_count), 100), 'physician'] = random.sample(range(physician_count + 1), 100)
    df_trained_in.loc[random.randint(0, physician_count), 'treatment'] = random.randint(1, department_count)

df_trained_in.to_csv("trained_in_table.csv", index=False)


df_nurse = pd.read_csv("nurse_table.csv")
print(df_nurse['employee_id'])
df_nurse['employee_id'] = df_nurse['employee_id'].astype(int)
nurse_position_list = ("Nursing assistant (CNA)", "Licensed practical nurse (LPN)", "Registered nurse (RN)",
                       "Advanced practice registered nurses (APRNs)")
for _ in range(0,nurse_count):
    df_nurse.loc[random.randint(0, nurse_count), 'position'] = random.choice(nurse_position_list)
df_nurse.to_csv("nurse_table.csv", index=False)


df_exel = pd.read_excel('Medicines_output_herbal_medicines.xlsx', sheet_name='Worksheet 1')
name_list = df_exel['name'].tolist()
brand_list = df_exel['brand'].tolist()
use_list = df_exel['description'].tolist()

df_medication = pd.read_csv("medication_table.csv")
df_medication['name'] = name_list
df_medication['brand'] = brand_list
df_medication['description'] = use_list

df_medication.to_csv("medication_table.csv", index=False)


df_block = pd.read_csv("block_table.csv")
for i in range(0, block_count):
    df_block['code'].values[i] = random.randint(10000, 99999)
    df_block.to_csv("block_table.csv", index=False)
df_block = pd.read_csv("room_table.csv")


df_room = pd.read_csv("room_table.csv")
for i in range(0,room_count):
    df_room['block_floor_code'].values[i] = random.randint(1, block_count)
df_room.to_csv('room_table.csv', index=False)



def add_start_days(startdate) :
    end_date = pd.to_datetime(startdate) + pd.DateOffset(days=random.randint(1, 8))
    return end_date


df_on_call = pd.read_csv("on_call_table.csv")

for i in range(0,nurse_count):
    df_on_call.loc[random.sample(range(0, nurse_count), 100), 'nurse'] = random.sample(range(0, nurse_count), 100)
    df_on_call.loc[random.sample(range(0, nurse_count), 100), 'physician'] = random.sample(range(0, physician_count), 100)
    df_on_call['block_floor_code'].values[i] = random.randint(1, block_count)
    df_on_call['physician'] = df_on_call['physician'].astype(int)

df_on_call.to_csv('on_call_table.csv', index=False)

