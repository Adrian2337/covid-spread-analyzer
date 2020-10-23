from firebase_admin import db
import random


def save_data_example(json_file):
    ref = db.reference()
    json_file = {
        'dolnośląskie': {
            'covid_cases': 3,
            'covid_deaths': 2,
            'covid_recovered': 2
        },
        'kujawsko-pomorskie': {
            'covid_cases': 3,
            'covid_deaths': 2,
            'covid_recovered': 2
        },
        'lubelskie': {
            'covid_cases': 3,
            'covid_deaths': 2,
            'covid_recovered': 2
        },
        'małopolskie': {
            'covid_cases': 3,
            'covid_deaths': 2,
            'covid_recovered': 2
        },
        'mazowieckie': {
            'covid_cases': 3,
            'covid_deaths': 2,
            'covid_recovered': 2
        },
        'opolskie': {
            'covid_cases': 3,
            'covid_deaths': 2,
            'covid_recovered': 2
        }
    }
    ref.child('date' + str(random.randint(0, 10 ** 10))).set(json_file)
