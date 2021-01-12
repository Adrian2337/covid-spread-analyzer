from data_fetch.twitter.DictPackager import DictPackager
from data_fetch.twitter.DataPack import DataPack
import unittest


class TestDictPackager(unittest.TestCase):

    def test_prepare_dicts(self):
        dp1 = DataPack(
            "1-01-01",
            100,
            200,
            300,
            400,
            500,
            {
                "Dolnośląskie": {"daily infected": 1},
                "Kujawsko-pomorskie": {"daily infected": 1},
                "Lubelskie": {"daily infected": 1},
                "Lubuskie": {"daily infected": 1},
                "Łódzkie": {"daily infected": 1},
                "Małopolskie": {"daily infected": 1},
                "Mazowieckie": {"daily infected": 1},
                "Opolskie": {"daily infected": 1},
                "Podkarpackie": {"daily infected": 1},
                "Podlaskie": {"daily infected": 1},
                "Pomorskie": {"daily infected": 1},
                "Śląskie": {"daily infected": 1},
                "Świętokrzyskie": {"daily infected": 1},
                "Warmińsko-mazurskie": {"daily infected": 1},
                "Wielkopolskie": {"daily infected": 1},
                "Zachodniopomorskie": {"daily infected": 1}
            }
        )

        dp2 = DataPack(
            "2-02-02",
            1000,
            2000,
            3000,
            4000,
            5000,
            {
                "Dolnośląskie": {"daily infected": 10},
                "Kujawsko-pomorskie": {"daily infected": 10},
                "Lubelskie": {"daily infected": 10},
                "Lubuskie": {"daily infected": 10},
                "Łódzkie": {"daily infected": 10},
                "Małopolskie": {"daily infected": 10},
                "Mazowieckie": {"daily infected": 10},
                "Opolskie": {"daily infected": 10},
                "Podkarpackie": {"daily infected": 10},
                "Podlaskie": {"daily infected": 10},
                "Pomorskie": {"daily infected": 10},
                "Śląskie": {"daily infected": 10},
                "Świętokrzyskie": {"daily infected": 10},
                "Warmińsko-mazurskie": {"daily infected": 10},
                "Wielkopolskie": {"daily infected": 10},
                "Zachodniopomorskie": {"daily infected": 10}
            }
        )

        data = DictPackager.prepare_dicts([dp1, dp2])
        self.assertEqual(data["Last Update Date"], "2-02-02")
        self.assertEqual(data["Map Data"]["1-01-01"]["daily infected"], 100)
