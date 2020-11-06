from data_fetch.twitter.ApiWrapper import ApiWrapper
from data_fetch.twitter.TweetCollector import TweetCollector
from data_fetch.twitter.CovidDataYielder import CovidDataYielder


def main():
    consumer = ""
    consumer_secret = ""
    token = ""
    token_secret = ""

    api_wrapper = ApiWrapper(consumer, consumer_secret, token, token_secret)
    tweet_collector = TweetCollector(api_wrapper)
    covid_data_yielder = CovidDataYielder(tweet_collector)

    print(covid_data_yielder.yield_data("2020-11-04"), sep="\n\n")


if __name__ == "__main__":
    main()