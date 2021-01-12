from data_fetch.twitter.TweetCollector import TweetCollector
from datetime import datetime
import unittest


class TestTweetCollector(unittest.TestCase):

    def test_collect_tweets(self):
        class TweetMock:
            def __init__(self, date, idd):
                self.created_at = date
                self.id = idd

        class ApiWrapper:
            def get_mz_tweets(self, before_id=None):
                if before_id is None:
                    return [TweetMock(datetime(year=1346, month=8, day=26), 50_000)] * 10
                elif before_id == 50_000:
                    return [TweetMock(datetime(year=1337, month=1, day=1), 40_000)] * 20
                else:
                    return []

        tweet_collector = TweetCollector(ApiWrapper())

        last_data_download_date = "1350-01-01"
        tweets = tweet_collector.collect_tweets(last_data_download_date)
        self.assertEqual(len(tweets), 10)

        last_data_download_date = "1340-01-01"
        tweets = tweet_collector.collect_tweets(last_data_download_date)
        self.assertEqual(len(tweets), 30)

        last_data_download_date = "1330-01-01"
        tweets = tweet_collector.collect_tweets(last_data_download_date)
        self.assertEqual(len(tweets), 30)
