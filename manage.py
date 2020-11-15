#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from firebase_admin import credentials, initialize_app

from covid_spread_analyzer.prediction_app.predictioner import Predictioner
from data_fetch.twitter.DataYieldService import DataYieldService
from covid_spread_analyzer.DBUpdateService import DBUpdateService
from covid_spread_analyzer.UpdateService import UpdateService
import json
from covid_spread_analyzer.database_operations import *


def main():
    # app setup
    cred = credentials.Certificate('firebase_files/covid-spread-analyzer-firebase-adminsdk-hxchu-8c78edc7cd.json')
    initialize_app(cred, {
        'databaseURL': 'https://covid-spread-analyzer.firebaseio.com/'
    })
    DataYieldService.initialize()
    UpdateService.start()
    # todo: resolve bug which double-starts the app (seen in UpdateService and before on DBUpdateService)
    # save_data_all(
    #    DataYieldService.yield_data_since("2020-10-24", last_relevant_date="2020-11-08", include_first_day=True))
    # save_data({"Last Update Date": "2020-10-26"})
    # print(load_data("Last Update Date"))
    # DBUpdateService.update_database()

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covid_spread_analyzer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
