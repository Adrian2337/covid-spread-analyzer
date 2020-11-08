#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from firebase_admin import credentials, initialize_app

from data_fetch.twitter.DataYieldService import DataYieldService
import json
from covid_spread_analyzer.database_operations import *


def main():
    # app setup
    cred = credentials.Certificate('firebase_files/covid-spread-analyzer-firebase-adminsdk-hxchu-8c78edc7cd.json')
    initialize_app(cred, {
        'databaseURL': 'https://covid-spread-analyzer.firebaseio.com/'
    })
    #DataYieldService.initialize()
    #ex = DataYieldService.yield_data_since("2020-11-02")
    #print(ex)
    # load_data("2020", "11", "01", "daily deceased")
    #save_data(ex[0])
    #save_data(ex[1])
    DataYieldService.initialize()
    # print(json.dumps(DataYieldService.yield_data_since("2020-11-03", last_relevant_date="2020-11-04",
    #                                                  include_first_day=True), indent=4, ensure_ascii=False))

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
