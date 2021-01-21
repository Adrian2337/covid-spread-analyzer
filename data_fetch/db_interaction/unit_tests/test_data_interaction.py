from data_fetch.db_interaction import data_interaction
import unittest


class TestDataInteraction(unittest.TestCase):

    def test_merge(self):
        old_data = {
            "Map Data": {
                "9-10-01": {
                    "date": "9-10-01",
                    "daily infected": 40_000,
                    "daily deceased": 25_000,
                    "Voivodeships": {
                        "Teutoburg": {
                            "daily infected": 3
                        }
                    }
                }
            },
            "Poland": {
                "9-10-01": {
                    "date": "9-10-01",
                    "daily infected": 40_000,
                    "daily deceased": 25_000,
                }
            },
            "Voivodeships": {
                "Teutoburg": {
                    "9-10-01": {
                        "date": "9-10-01",
                        "daily infected": 3
                    }
                }
            }
        }

        new_data = {
            "Map Data": {
                "9-10-01": {
                    "date": "9-10-01",
                    "daily infected": 40_001,
                    "daily deceased": 24_999,
                    "daily cured": 500,
                    "Voivodeships": {
                        "Teutoburg": {
                            "daily infected": 4,
                            "daily deceased": 2
                        }
                    }
                }
            },
            "Poland": {
                "9-10-01": {
                    "date": "9-10-01",
                    "daily infected": 40_001,
                    "daily deceased": 24_999,
                    "daily cured": 500,
                }
            },
            "Voivodeships": {
                "Teutoburg": {
                    "9-10-01": {
                        "date": "9-10-01",
                        "daily infected": 4,
                        "daily deceased": 2
                    }
                }
            }
        }

        merged = data_interaction.merge(new_data=new_data, old_data=old_data)
        self.assertEqual(merged["Map Data"]["9-10-01"]["daily infected"], 40_000)
        self.assertEqual(merged["Map Data"]["9-10-01"]["daily cured"], 500)
        self.assertEqual(merged["Voivodeships"]["Teutoburg"]["9-10-01"]["daily deceased"], 2)
        self.assertEqual(merged["Voivodeships"]["Teutoburg"]["9-10-01"]["daily infected"], 3)
