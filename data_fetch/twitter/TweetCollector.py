from data_fetch.twitter.ApiWrapper import ApiWrapper


class TweetCollector:

    def __init__(self, api_wrapper: ApiWrapper):
        self.api_wrapper = api_wrapper

    def collect_tweets(self, last_data_download_date):
        tweets = self.api_wrapper.get_mz_tweets()
        while tweets[-1].created_at.strftime("%Y-%m-%d") >= last_data_download_date:
            additional_tweets = self.api_wrapper.get_mz_tweets(before_id=tweets[-1].id)
            if not additional_tweets:
                print("Failed to collect all wanted tweets.")
                print("Last one collected is from", tweets[-1].created_at.strftime("%Y-%m-%d"))
                break
            tweets += additional_tweets
        return tweets[::-1]
