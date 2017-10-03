"""
File: term_frequency.py
Language: Python 3.5.2
Description: Feature extraction using TF-IDF
"""
import codecs
import math
from textblob import TextBlob as tb
from nltk.corpus import stopwords

POSITIVE_TWEETS = "./data/positive_tweets"
NEGATIVE_TWEETS = "./data/negative_tweets"
NEUTRAL_TWEETS = "./data/neutral_tweets"

FILE_LIST = [POSITIVE_TWEETS, NEGATIVE_TWEETS, NEUTRAL_TWEETS]


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


def main():
    bloblist = []
    custom_stopwords = set(codecs.open("./inputs/custom_stopwords", 'r', 'utf-8').read().splitlines())
    stop_words = set(stopwords.words('english'))
    all_stop_words = custom_stopwords | stop_words
    for path in FILE_LIST:
        with open(path, encoding="utf-8") as input_file:
            content = input_file.read().lower()
            bloblist.append(tb(content))
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words if word not in all_stop_words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:100]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


if __name__ == "__main__":
    main()
