from data_fetch.twitter.CovidDataYielder import CovidDataYielder
from data_fetch.twitter.ApiWrapper import ApiWrapper
from data_fetch.twitter.TweetCollector import TweetCollector
from data_fetch.twitter.CovidDataYielder import CovidDataYielder
from datetime import datetime


class DataYieldService:
    covid_data_yielder = None

    @staticmethod
    def initialize():
        with open("keys.txt", "r") as f:
            consumer, consumer_secret, token, token_secret, _ = f.read().split("\n")

        api_wrapper = ApiWrapper(consumer, consumer_secret, token, token_secret)
        tweet_collector = TweetCollector(api_wrapper)
        DataYieldService.covid_data_yielder = CovidDataYielder(tweet_collector)

    @staticmethod
    def yield_data_since(date: str, last_relevant_date=datetime.now().strftime("%Y-%m-%d"),
                         include_first_day=False) -> list:
        return DataYieldService.covid_data_yielder.yield_data(date, last_relevant_date, include_first_day)
