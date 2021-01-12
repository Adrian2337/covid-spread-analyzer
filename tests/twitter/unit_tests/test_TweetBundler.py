from data_fetch.twitter.TweetBundler import TweetBundler
from datetime import datetime
import unittest


class TestTweetBundler(unittest.TestCase):

    def test_bundle_tweets(self):
        class TweetMock:
            def __init__(self, date, text):
                self.created_at = date
                self.full_text = text
        country_time = datetime(year=966, month=1, day=1)
        millenium_time = datetime(year=1000, month=1, day=1)

        pt11 = "Mamy 6 919 nowych i potwierdzonych przypadków zakażenia #koronawirus z województw: mazowieckiego (890), wielkopolskiego (683), śląskiego (649), pomorskiego (582), zachodniopomorskiego (550), warmińsko-mazurskiego (549), kujawsko-pomorskiego (534), łódzkiego (393),"
        pt12 = "lubelskiego (357), dolnośląskiego (336), podlaskiego (329), małopolskiego (280), lubuskiego (201), podkarpackiego (192), opolskiego (138), świętokrzyskiego (125). 131 zakażeń to dane bez wskazania adresu, które zostaną uzupełnione przez inspekcję sanitarną."
        pt13 = """Z powodu COVID-19 zmarło 106 osób, natomiast z powodu współistnienia COVID-19 z innymi schorzeniami zmarło 337 osób.

Liczba zakażonych koronawirusem: 1 450 747/34 141  (wszystkie pozytywne przypadki/w tym osoby zmarłe)."""
        pt14 = "📊 W ciągu doby wykonano ponad 48,3 tys. testów na #koronawirus."

        pt21 = "Mamy 4835 nowych i potwierdzonych przypadków zakażenia #koronawirus z województw: mazowieckiego (683), kujawsko-pomorskiego (438), wielkopolskiego (413), pomorskiego (411), zachodniopomorskiego (392), śląskiego (368), warmińsko-mazurskiego (354), dolnośląskiego (311),"
        pt22 = "łódzkiego (275), lubelskiego (266), małopolskiego (234), podkarpackiego (188), podlaskiego (126), opolskiego (95), lubuskiego (85), świętokrzyskiego (77). 119 zakażeń to dane bez wskazania adresu, które zostaną uzupełnione przez inspekcję sanitarną."
        pt23 = """Z powodu COVID-19 zmarło 60 osób, natomiast z powodu współistnienia COVID-19 z innymi schorzeniami zmarło 231 osób.

Liczba zakażonych koronawirusem: 1 443 804/33 698  (wszystkie pozytywne przypadki/w tym osoby zmarłe)."""
        pt24 = "📊 W ciągu doby wykonano ponad 48,4 tys. testów na #koronawirus."

        tweets_mock = [
            TweetMock(country_time, pt11),
            TweetMock(country_time, pt12),
            TweetMock(country_time, pt13),
            TweetMock(country_time, "Hello there!"),
            TweetMock(country_time, "General Kenobi!"),
            TweetMock(country_time, "You are a bold one!"),
            TweetMock(country_time, pt14),
            TweetMock(country_time, "Lorem ipsum"),

            TweetMock(millenium_time, pt21),
            TweetMock(millenium_time, pt22),
            TweetMock(millenium_time, pt23),
            TweetMock(millenium_time, pt24)
        ]

        tweet_bundles = TweetBundler.bundle_tweets(tweets_mock)
        self.assertEqual(len(tweet_bundles), 2)
        self.assertEqual(tweet_bundles[0].text, " ".join([pt11, pt12, pt13, pt14]))
        self.assertEqual(tweet_bundles[0].date, "966-01-01")
        self.assertEqual(tweet_bundles[1].text, " ".join([pt21, pt22, pt23, pt24]))
        self.assertEqual(tweet_bundles[1].date, "1000-01-01")
