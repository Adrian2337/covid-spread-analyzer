from data_fetch.twitter.TweetCollector import TweetCollector
from data_fetch.twitter.TweetBundler import TweetBundler
from data_fetch.twitter.DataMiner import DataMiner


class CovidDataYielder:

    def __init__(self, tweet_collector: TweetCollector):
        self.tweet_collector = tweet_collector

    def yield_data(self, last_gotten_date) -> list:
        data = []

        tweets = self.tweet_collector.collect_tweets(last_gotten_date)
        bundles = TweetBundler.bundle_tweets(tweets)
        for b in bundles:
            if b.date > last_gotten_date:
                data_dict = DataMiner.prepare_dictionary(b)
                data.append(data_dict)

        return data
