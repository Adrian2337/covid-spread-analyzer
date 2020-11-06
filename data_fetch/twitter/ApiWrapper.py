import tweepy


class ApiWrapper:

    def __init__(self, consumer_key: str, consumer_secret: str,
                 access_token: str, access_token_secret: str):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_mz_tweets(self, amount=20, before_id=None) -> list:
        if before_id:
            return self.api.user_timeline(screen_name="MZ_GOV_PL",
                                          count=amount,
                                          include_rts=True,
                                          max_id=(before_id-1),
                                          tweet_mode="extended")
        else:
            return self.api.user_timeline(screen_name="MZ_GOV_PL",
                                          count=amount,
                                          include_rts=True,
                                          tweet_mode="extended")
