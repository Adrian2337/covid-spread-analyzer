from data_fetch.twitter.TweetCollector import TweetCollector
from data_fetch.twitter.TweetBundler import TweetBundler
from data_fetch.twitter.DataMiner import DataMiner
from data_fetch.twitter.DictPackager import DictPackager


class CovidDataYielder:

    def __init__(self, tweet_collector: TweetCollector):
        self.tweet_collector = tweet_collector

    def yield_data(self, last_gotten_date: str) -> list:
        data_packs = []

        tweets = self.tweet_collector.collect_tweets(last_gotten_date)
        bundles = TweetBundler.bundle_tweets(tweets)
        for b in bundles:
            if b.date > last_gotten_date:
                data_pack = DataMiner.prepare_data_pack(b)
                data_packs.append(data_pack)

        data = DictPackager.prepare_dicts(data_packs)
        return data
