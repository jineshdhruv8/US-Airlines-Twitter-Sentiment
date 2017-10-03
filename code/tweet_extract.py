"""
File: tweet_extract.py
Language: Python 3.5.2
Description: Extract tweets to respective document.
"""
import csv

CLEANED_FILE_PATH = "./data/cleaned_data"
POSITIVE_TWEETS = "./data/positive_tweets"
NEGATIVE_TWEETS = "./data/negative_tweets"
NEUTRAL_TWEETS = "./data/neutral_tweets"
POSITIVE = "positive"
NEGATIVE = "negative"
NEUTRAL = "neutral"


def extract():

    with open(CLEANED_FILE_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            category = row[1]
            tweet = row[10]
            if category == POSITIVE:
                with open(POSITIVE_TWEETS, 'a', encoding='utf-8') as positive_file:
                    positive_file.write(tweet + "\n")
            if category == NEGATIVE:
                with open(NEGATIVE_TWEETS, 'a', encoding='utf-8') as negative_file:
                    negative_file.write(tweet + "\n")
            if category == NEUTRAL:
                with open(NEUTRAL_TWEETS, 'a', encoding='utf-8') as neutral_file:
                    neutral_file.write(tweet + "\n")

if __name__ == '__main__':
    extract()
