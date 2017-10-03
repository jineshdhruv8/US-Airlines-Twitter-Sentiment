"""
File: twitter_data_streaming.py
Language: Python 3.5.2
Description: Streaming real time tweets using Twitter streaming API
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "access_token"
access_token_secret = "access_token_secret"
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        content = ""
        if status.text is not None and status.lang == 'en' and "RT" not in status.text:
            content = "#*TWEET*# " + status.text + "\n"
            with open("./twitter_data/tweets", "a", encoding="utf-8") as csvfile:
                csvfile.write(content)

    def on_error(self, status_code):
        if status_code == 420:
            return False


def main():
    stream_listener = StreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, stream_listener)
    stream.filter(track=["SouthwestAir", "JetBlue", "VirginAmerica", "@United"])


if __name__ == "__main__":
    main()
