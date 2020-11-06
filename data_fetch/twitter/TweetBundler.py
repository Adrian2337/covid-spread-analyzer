from parse import search
from data_fetch.twitter.InfoBundle import InfoBundle


class TweetBundler:

    patterns = {
        "report_initial": "Mamy {} now{} i potwierdzon{} przypad{} zakażenia #koronawirus z województw:",
        "report_final": "Liczba zakażonych koronawirusem: {}/{}(wszystkie pozytywne przypadki/w tym osoby zmarłe).",
        "report_tests": "W ciągu doby wykonano ponad {} testów na #koronawirus."
    }

    @staticmethod
    def bundle_tweets(tweets):
        info_bundles = []
        i = 0
        while i < len(tweets):
            if search(TweetBundler.patterns["report_initial"], tweets[i].full_text):
                first_tweet_no = i
                i += 1
                while not search(TweetBundler.patterns["report_final"], tweets[i].full_text):
                    i += 1
                i += 1
                report = tweets[first_tweet_no:i]
                while i < len(tweets) and not search(TweetBundler.patterns["report_tests"], tweets[i].full_text):
                    i += 1
                if i < len(tweets):
                    info_bundles.append(InfoBundle(report + [tweets[i]]))
                    i += 1
            else:
                i += 1
        return info_bundles
