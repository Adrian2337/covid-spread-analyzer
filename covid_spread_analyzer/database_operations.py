from collections import ChainMap

from firebase_admin import db
import random

root = 'cases-data'


def save_data(dictionary):
    ref = db.reference().child(root)
    for year in dictionary:
        ref = ref.child(year)
        for month in dictionary[year]:
            ref = ref.child(month)
            for day in dictionary[year][month]:
                ref = ref.child(day)
                ref.update(dictionary[year][month][day])


def load_data(*args):
    ref = db.reference().child(root)
    for x in args:
        ref = ref.child(x)
    data = ref.get()
    print('loaded-> ', data, '<-end of loading')
    return data
