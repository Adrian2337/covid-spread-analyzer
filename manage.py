#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from data_fetch.twitter.DataYieldService import DataYieldService
import json


def main():
    # app setup
    DataYieldService.initialize()
    # print(json.dumps(DataYieldService.yield_data_since("2020-11-05"), indent=4, ensure_ascii=False))

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
