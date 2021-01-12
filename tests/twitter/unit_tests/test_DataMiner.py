from data_fetch.twitter.DataMiner import DataMiner
from datetime import datetime
import unittest


class TestDataMiner(unittest.TestCase):

    def test_prepare_data_pack(self):
        class InfoBundle:
            def __init__(self, date, txt):
                self.date = date
                self.text = txt
        homage_date = datetime(year=1525, month=4, day=10)
        text = """Mamy 6 919 nowych i potwierdzonych przypadków zakażenia #koronawirus z województw: mazowieckiego (890), wielkopolskiego (683), śląskiego (649), pomorskiego (582), zachodniopomorskiego (550), warmińsko-mazurskiego (549), kujawsko-pomorskiego (534), łódzkiego (393), lubelskiego (357), dolnośląskiego (336), podlaskiego (329), małopolskiego (280), lubuskiego (201), podkarpackiego (192), opolskiego (138), świętokrzyskiego (125). 131 zakażeń to dane bez wskazania adresu, które zostaną uzupełnione przez inspekcję sanitarną. Z powodu COVID-19 zmarło 106 osób, natomiast z powodu współistnienia COVID-19 z innymi schorzeniami zmarło 337 osób.

Liczba zakażonych koronawirusem: 1 450 747/34 141  (wszystkie pozytywne przypadki/w tym osoby zmarłe). 📊 W ciągu doby wykonano ponad 48,3 tys. testów na #koronawirus."""
        info_bundle = InfoBundle(homage_date, text)

        data_pack = DataMiner.prepare_data_pack(info_bundle)
        self.assertEqual(data_pack.date, homage_date)
        self.assertEqual(data_pack.daily_cases, 6919)
        self.assertEqual(data_pack.daily_deaths, 443)
        self.assertEqual(data_pack.daily_tests, 48_300)
        self.assertEqual(data_pack.total_cases, 1_450_747)
        self.assertEqual(data_pack.total_deaths, 34_141)

        self.assertEqual(data_pack.voivodeship_stats["Mazowieckie"]["daily infected"], 890)
        self.assertEqual(data_pack.voivodeship_stats["Wielkopolskie"]["daily infected"], 683)
        self.assertEqual(data_pack.voivodeship_stats["Śląskie"]["daily infected"], 649)
        self.assertEqual(data_pack.voivodeship_stats["Pomorskie"]["daily infected"], 582)
        self.assertEqual(data_pack.voivodeship_stats["Zachodniopomorskie"]["daily infected"], 550)
        self.assertEqual(data_pack.voivodeship_stats["Warmińsko-mazurskie"]["daily infected"], 549)
        self.assertEqual(data_pack.voivodeship_stats["Kujawsko-pomorskie"]["daily infected"], 534)
        self.assertEqual(data_pack.voivodeship_stats["Łódzkie"]["daily infected"], 393)
        self.assertEqual(data_pack.voivodeship_stats["Lubelskie"]["daily infected"], 357)
        self.assertEqual(data_pack.voivodeship_stats["Dolnośląskie"]["daily infected"], 336)
        self.assertEqual(data_pack.voivodeship_stats["Podlaskie"]["daily infected"], 329)
        self.assertEqual(data_pack.voivodeship_stats["Małopolskie"]["daily infected"], 280)
        self.assertEqual(data_pack.voivodeship_stats["Lubuskie"]["daily infected"], 201)
        self.assertEqual(data_pack.voivodeship_stats["Podkarpackie"]["daily infected"], 192)
        self.assertEqual(data_pack.voivodeship_stats["Opolskie"]["daily infected"], 138)
        self.assertEqual(data_pack.voivodeship_stats["Świętokrzyskie"]["daily infected"], 125)
