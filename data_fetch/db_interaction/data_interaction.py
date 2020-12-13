import data_preparation
import json
from datetime import datetime
from copy import deepcopy


def update_data(start_date, end_date=datetime.now().strftime("%Y-%m-%d")):
    with open("data.json", "r") as f:
        old_data = json.load(f)
    new_data = data_preparation.prepare_new_data(start_date, end_date)
    mix = merge(old_data, new_data)
    with open("data.json", "w") as f:
        json.dump(mix, f, indent=4, ensure_ascii=False)


def merge(old_data, new_data):
    data = deepcopy(new_data)

    for date in new_data["Map Data"].keys():
        if date in old_data["Map Data"].keys() and old_data["Map Data"][date]:
            for k in old_data["Map Data"][date].keys():
                if k != "Voivodeships":
                    data["Map Data"][date][k] = old_data["Map Data"][date][k]
                else:
                    for v in old_data["Map Data"][date]["Voivodeships"].keys():
                        for k1 in old_data["Map Data"][date]["Voivodeships"][v].keys():
                            data["Map Data"][date]["Voivodeships"][v][k1] = \
                                old_data["Map Data"][date]["Voivodeships"][v][k1]

    for date in new_data["Poland"].keys():
        if date in old_data["Poland"].keys() and old_data["Poland"][date]:
            for k in old_data["Poland"][date].keys():
                data["Poland"][date][k] = old_data["Poland"][date][k]

    for voivodeship in new_data["Voivodeships"].keys():
        for date in new_data["Voivodeships"][voivodeship].keys():
            if date in old_data["Voivodeships"][voivodeship].keys() and old_data["Voivodeships"][voivodeship][date]:
                for k in old_data["Voivodeships"][voivodeship][date].keys():
                    data["Voivodeships"][voivodeship][date][k] = old_data["Voivodeships"][voivodeship][date][k]

    return data
