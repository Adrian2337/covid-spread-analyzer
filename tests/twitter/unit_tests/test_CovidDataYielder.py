from data_fetch.twitter.CovidDataYielder import CovidDataYielder
from data_fetch.twitter.TweetBundler import TweetBundler
from data_fetch.twitter.DataMiner import DataMiner
from data_fetch.twitter.DictPackager import DictPackager
import unittest


class TestCovidDataYielder(unittest.TestCase):

    def test_yield_data(self):
        class TweetCollector:
            def collect_tweets(self, last_gotten_date):
                pass

        class InfoBundle:
            def __init__(self, date):
                self.date = date

        def bundle_tweets_monkey(tweets):
            return [
                InfoBundle("1111-12-12"),
                InfoBundle("1222-12-12"),
                InfoBundle("1333-12-12")
            ]

        def prepare_data_pack_monkey(b):
            return None

        def prepare_dicts_monkey(data_packs):
            return data_packs

        covid_data_yielder = CovidDataYielder(TweetCollector())
        bundle_tweets = TweetBundler.bundle_tweets
        TweetBundler.bundle_tweets = bundle_tweets_monkey
        prepare_data_pack = DataMiner.prepare_data_pack
        DataMiner.prepare_data_pack = prepare_data_pack_monkey
        prepare_dicts = DictPackager.prepare_dicts
        DictPackager.prepare_dicts = prepare_dicts_monkey

        data = covid_data_yielder.yield_data("1111-12-11", "1300-12-12")
        self.assertEqual(len(data), 2)

        data = covid_data_yielder.yield_data("1111-12-11", "1400-12-12")
        self.assertEqual(len(data), 3)

        TweetBundler.bundle_tweets = bundle_tweets
        DataMiner.prepare_data_pack = prepare_data_pack
        DictPackager.prepare_dicts = prepare_dicts
