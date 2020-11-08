from data_fetch.twitter.TweetCollector import TweetCollector
from data_fetch.twitter.TweetBundler import TweetBundler
from data_fetch.twitter.DataMiner import DataMiner
from data_fetch.twitter.DictPackager import DictPackager
from datetime import datetime


class CovidDataYielder:

    def __init__(self, tweet_collector: TweetCollector):
        self.tweet_collector = tweet_collector

    def yield_data(self, last_gotten_date: str, last_relevant_date=datetime.now().strftime("%Y-%m-%d"),
                   include_first_day=False) -> list:
        data_packs = []

        tweets = self.tweet_collector.collect_tweets(last_gotten_date)
        bundles = TweetBundler.bundle_tweets(tweets)
        for b in bundles:
            if (b.date > last_gotten_date or (b.date == last_gotten_date and include_first_day)) and \
                    b.date <= last_relevant_date:
                data_pack = DataMiner.prepare_data_pack(b)
                data_packs.append(data_pack)

        data = DictPackager.prepare_dicts(data_packs)
        return data
