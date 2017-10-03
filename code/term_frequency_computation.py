"""
File: term_frequency_computation.py
Language: Python 3.5.2
Description: Feature extraction using bag-of-words approach
"""

import sys
import codecs
import nltk
from nltk.corpus import stopwords

POSITIVE_TWEETS = "./data/positive_tweets"
NEGATIVE_TWEETS = "./data/negative_tweets"
NEUTRAL_TWEETS = "./data/neutral_tweets"


def get_word_count():
    stop_words = set(stopwords.words('english'))
    custom_stopwords = set(codecs.open("./inputs/custom_stopwords", 'r', 'utf-8').read().splitlines())
    all_stopwords = stop_words | custom_stopwords
    filename = POSITIVE_TWEETS
    input_file = codecs.open(filename, 'r', 'utf-8')
    content = nltk.word_tokenize(input_file.read())
    content = [word for word in content if len(word) > 1]
    content = [word for word in content if not word.isnumeric()]
    content = [word.lower() for word in content]
    content = [word for word in content if word not in all_stopwords]
    word_frequency = nltk.FreqDist(content)
    for word, count in word_frequency.most_common(100):
        print("{} : {}".format(word, count))

    return word_frequency

if __name__ == "__main__":
    get_word_count()
