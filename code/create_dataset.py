"""
File: create_dataset.py
Language: Python 3.5.2
Description: Creates training and testing set.
"""

POSITIVE = "Positive"
NEGATIVE = "Negative"
NEUTRAL = "Neutral"
TRAINING_DATA = "./dataset/training_data.csv"
FEATURES = "./inputs/features"
SENTIMENTS = "./inputs/sentiment_words"
NEGATIVE_FEEDBACK = "./data/negative_feedback"
NEGATIVE_WORDS = "./inputs/negative_words"

WORD_LIST = []
with open(NEGATIVE_FEEDBACK) as input_file:
    for l in input_file:
        WORD_LIST.append(l.strip())

WORDS = []
with open(NEGATIVE_WORDS, encoding='utf-8') as word_file:
    for l in word_file:
        WORDS.append(l.strip())

SENTIMENT_LIST = []
with open(SENTIMENTS, encoding='utf-8') as word_file:
    for l in word_file:
        SENTIMENT_LIST.append(l.strip())


def create_dataset(features_path, tweets, training_data, sentiments, tag):
    feature_list = []
    with open(features_path, encoding='utf-8') as input_file:
        for line in input_file:
            feature_list.append(line.strip())

    with open(tweets, encoding="utf-8") as tweet_file:
        for line in tweet_file:
            add_record(line.lower(), feature_list, training_data, sentiments, tag)


def add_record(tweet, feature_list, training_dataset, sentiments, tag):
    record = []
    for feature in feature_list:
        count = 0
        if feature in tweet:
            if tag == POSITIVE and look_negative_sentiments(feature):
                count = 1
            if tag == NEGATIVE and look_negative_words(tweet, feature):
                count = 1
            if tag == NEUTRAL and look_negative_sentiments(feature) and look_negative_words(tweet, feature):
                count = 1

        record.append(count)
    record.append(tag + "\n")
    data = ",".join(map(str, record))

    with open(training_dataset, 'a') as output_file:
        output_file.write(data)


def look_negative_sentiments(feature):
    if feature in WORD_LIST:
        return False
    return True


def look_negative_words(line, feature):
    if feature not in SENTIMENT_LIST:
        return True
    for word in WORDS:
        if word in line:
            return False
    return True


def main():
    tweet_file_path = "./data/negative_tweets"
    create_dataset(FEATURES, tweet_file_path, TRAINING_DATA, SENTIMENTS, NEGATIVE)


if __name__ == '__main__':
    main()
