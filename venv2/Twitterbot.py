import Twitterset
import fire

import tweepy


class Twitterbot:

    def get_tweets(self, name):
        if __name__ == "__main__":
            fire.Fire(Twitterset.download_tweets(name))

    def set_tweet(self, tweet: str):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
        auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        api.update_status("Hello Tweepy")
