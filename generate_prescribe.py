import pandas as pd
import random
import string
from faker import Faker

medication_count = 200
physician_count = 100


class Prescribe:
    def __init__(self, physician, patient, medication, date, appointment, dose):
        self.physician = physician
        self.patient = patient
        self.medication = medication
        self.date = date
        self.appointment = appointment
        self.dose = dose

    def __iter__(self):
        yield self.physician
        yield self.patient
        yield self.medication
        yield self.date
        yield self.appointment
        yield self.dose


faker = Faker()

def df_creation(min_patientID, max_patientID):
    prescribes = []

    for i in range(min_patientID + 1, max_patientID + 1):
        physician = random.randint(1, physician_count)
        patient = i
        medication = random.randint(1, medication_count)
        date = faker.date_time_between(start_date="-6y", end_date="now")
        appointment = i
        dose = random.randint(1, 500)

        prescribe = Prescribe(physician, patient, medication, date, appointment, dose)
        prescribes.append(prescribe)
    print(pd.DataFrame(prescribes))
    return pd.DataFrame(prescribes)

