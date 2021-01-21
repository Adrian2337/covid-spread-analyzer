from data_fetch.twitter.InfoBundle import InfoBundle
from datetime import datetime
import unittest


class TestInfoBundle(unittest.TestCase):

    def test_creation(self):
        class TweetMock:
            def __init__(self, date, text):
                self.created_at = date
                self.full_text = text
        battle_time = datetime(year=1410, month=7, day=15, hour=12, minute=30, second=37)
        tweets_mock = [
            TweetMock(battle_time, "Hello there!\n"),
            TweetMock(battle_time, "General Kenobi!"),
            TweetMock(battle_time, "You are a bold one!")
        ]

        info_bundle = InfoBundle(tweets_mock)
        self.assertEqual(info_bundle.date, "1410-07-15")
        self.assertEqual(info_bundle.text, "Hello there!\n General Kenobi! You are a bold one!")
