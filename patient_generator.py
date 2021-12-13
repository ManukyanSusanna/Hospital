import pandas as pd
from faker import Faker

patient_count = 10
physician_count = 100

class Patient:
    def __init__(self, ssn, name, address, phone, insurance_id, pcp):
        self.ssn = ssn
        self.name = name
        self.address = address
        self.phone = phone
        self.insurance_id = insurance_id
        self.pcp = pcp

    def __iter__(self):
        yield self.ssn
        yield self.name
        yield self.address
        yield self.phone
        yield self.insurance_id
        yield self.pcp


faker = Faker()
patients = []

for i in range(0,patient_count):
    ssn = str(faker.random_int(100, 999)) + '-' + str(faker.random_int(10, 99)) + '-' +str(faker.random_int(1000, 9999))
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    insurance_id = faker.random.randint(100000, 999999)
    pcp = faker.random.randint(1, physician_count)
    patient = Patient(ssn, name, address, phone, insurance_id, pcp)

    patients.append(patient)

df_patient = pd.DataFrame(patients)

# fields = ['ssn','name','address','phone','insurance_id','pcp']
# print(df_patient)
# filename = "patient_table.csv"
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     df_patient = pd.DataFrame(patients)
#     df_patient.to_csv("patient_table.csv", index=False, header=fields)
#

