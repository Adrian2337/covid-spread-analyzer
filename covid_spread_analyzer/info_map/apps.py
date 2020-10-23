from django.apps import AppConfig
from ..settings import DATABASES


class InfoMapConfig(AppConfig):
    name = 'covid_spread_analyzer.info_map'

    def ready(self):
        DATABASES.update({
        })
