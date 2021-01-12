from data_fetch.db_interaction import data_parse
import unittest


class TestDataParse(unittest.TestCase):

    def test_parse_all_for_country(self):
        with open("p.txt", "r") as f:
            site_text = f.read()
        data = data_parse.parse_all("Poland", site_text)

        self.assertEqual(data["2020-12-06"]["daily infected"], 9176)
        self.assertEqual(data["2020-12-06"]["total cured"], 706_720)

    def test_parse_all_for_voivodeship(self):
        with open("v.txt", "r") as f:
            site_text = f.read()
        data = data_parse.parse_all("Dolnośląskie", site_text)

        self.assertEqual(data["2020-12-06"]["daily infected"], 476)
        self.assertEqual(data["2020-12-06"]["total infected"], 74_892)
