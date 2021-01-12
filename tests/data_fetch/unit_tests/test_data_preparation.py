from data_fetch.db_interaction import data_preparation
from data_fetch.db_interaction import data_parse
import unittest


class TestDataPreparation(unittest.TestCase):

    def test_prepare_all_data(self):
        def parse_all_monkey(region_name, site_text):
            return site_text
        parse_all = data_parse.parse_all
        data_parse.parse_all = parse_all_monkey

        sites = {
            "Poland": "Poland",
            "Voivodeships": {
                "dolnoslaskie": "Dolnośląskie",
                "kujawsko-pomorskie": "Kujawsko-pomorskie",
                "lubelskie": "Lubelskie",
                "lubuskie": "Lubuskie",
                "lodzkie": "Łódzkie",
                "malopolskie": "Małopolskie",
                "mazowieckie": "Mazowieckie",
                "opolskie": "Opolskie",
                "podkarpackie": "Podkarpackie",
                "podlaskie": "Podlaskie",
                "pomorskie": "Pomorskie",
                "slaskie": "Śląskie",
                "swietokrzyskie": "Świętokrzyskie",
                "warminsko-mazurskie": "Warmińsko-mazurskie",
                "wielkopolskie": "Wielkopolskie",
                "zachodniopomorskie": "Zachodniopomorskie"
            }
        }

        data = data_preparation.prepare_all_data(sites)
        self.assertEqual(data["Poland"], "Poland")
        self.assertEqual(data["Voivodeships"]["Dolnośląskie"], "Dolnośląskie")

        data_parse.parse_all = parse_all

    def test_format_data(self):
        data = {
            "Poland": {
                "29-01-01": {
                    "daily infected": 123,
                    "daily deceased": 321
                },
                "29-02-01": {
                    "daily infected": 321,
                    "daily deceased": 123
                }
            },
            "Voivodeships": {
                "Dolnośląskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Kujawsko-pomorskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Lubelskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Lubuskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Łódzkie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Małopolskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Mazowieckie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Opolskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Podkarpackie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Podlaskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Pomorskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Śląskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Świętokrzyskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Warmińsko-mazurskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Wielkopolskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                },
                "Zachodniopomorskie": {
                    "29-01-01": {
                        "daily infected": 12,
                        "daily deceased": 21
                    }
                }
            }
        }

        formatted_data = data_preparation.format_data(data, "29-01-01", "29-01-31")
        self.assertEqual(formatted_data["Map Data"]["29-01-01"]["Voivodeships"]["Dolnośląskie"]["daily infected"], 12)
        self.assertIsNone(formatted_data["Map Data"]["29-01-01"]["daily cured"])
        self.assertNotIn("29-02-01", formatted_data["Poland"].keys())
