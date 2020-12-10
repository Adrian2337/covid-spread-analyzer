import sys
from datetime import datetime, timedelta
import json
import covid_spread_analyzer.database_operations as db
from firebase_admin import credentials, initialize_app

voivodeships = [
    "Dolnośląskie",
    "Kujawsko-pomorskie",
    "Lubelskie",
    "Lubuskie",
    "Łódzkie",
    "Małopolskie",
    "Mazowieckie",
    "Opolskie",
    "Podkarpackie",
    "Podlaskie",
    "Pomorskie",
    "Śląskie",
    "Świętokrzyskie",
    "Warmińsko-mazurskie",
    "Wielkopolskie",
    "Zachodniopomorskie"
]


def main():
    cred = credentials.Certificate('../../firebase_files/covid-spread-analyzer-firebase-adminsdk-hxchu-8c78edc7cd.json')
    initialize_app(cred, {
        'databaseURL': 'https://covid-spread-analyzer.firebaseio.com/'
    })

    if len(sys.argv) == 1:
        print(
            """Usage:
interact -d start_date [end_date]   # downloads database info from given date range
                                    # if end_date is not specified, does so till current day
                                    # dates have to be in YYYY-MM-DD format
interact -u                         # uploads data present to database
            """
        )
    elif sys.argv[1] == "-d":
        download(*get_dates())
    elif sys.argv[1] == "-u":
        upload()
    else:
        print("Invalid argument:", sys.argv[1])


def get_dates():
    start_date = sys.argv[2]
    end_date = sys.argv[3] if len(sys.argv) >= 4 else datetime.now().strftime("%Y-%m-%d")
    return start_date, end_date


def download(start_date, end_date):
    data = {
        "Map Data": dict(),
        "Poland": dict(),
        "Voivodeships": dict()
    }
    for v in voivodeships:
        data["Voivodeships"][v] = dict()

    for date in [
        (datetime.fromisoformat(start_date) + timedelta(days=x)).strftime("%Y-%m-%d") for x in range(
            0, (datetime.fromisoformat(end_date) - datetime.fromisoformat(start_date)).days + 1
        )
    ]:
        data["Map Data"][date] = db.load_data("Map Data", date)
        data["Poland"][date] = db.load_data("Poland", date)
        for v in voivodeships:
            data["Voivodeships"][v][date] = db.load_data("Voivodeships", v, date)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def upload():
    with open("data.json", "r") as f:
        data = json.load(f)

    for date in data["Map Data"].keys():
        db.save_data(data["Map Data"][date], "Map Data", date)

    for date in data["Poland"].keys():
        db.save_data(data["Poland"][date], "Poland", date)

    for voivodeship in data["Voivodeships"].keys():
        for date in data["Voivodeships"][voivodeship].keys():
            db.save_data(data["Voivodeships"][voivodeship][date], "Voivodeships", voivodeship, date)


if __name__ == "__main__":
    main()
