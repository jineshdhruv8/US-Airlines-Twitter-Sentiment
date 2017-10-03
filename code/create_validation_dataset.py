
"""
File: create_validation_dataset.py
Language: Python 3.5.2
Description: Using the tweets downloaded, validation dataset is generated.
"""

FEATURES = "./inputs/features"
NEGATIVE_WORDS = "./inputs/negative_words"
SENTIMENTS = "./inputs/sentiment_words"
VALIDATION_DATA = "./dataset/validation_data.csv"
TWEETS = "./twitter_data/tweets"

WORDS = []
with open(NEGATIVE_WORDS, encoding='utf-8') as word_file:
    for l in word_file:
        WORDS.append(l.strip())

SENTIMENT_LIST = []
with open(SENTIMENTS, encoding='utf-8') as word_file:
    for l in word_file:
        SENTIMENT_LIST.append(l.strip())


def create_dataset(features_path, tweets, data):
    feature_list = []
    with open(features_path, encoding='utf-8') as input_file:
        for line in input_file:
            feature_list.append(line.strip())

    with open(tweets, encoding="utf-8") as tweet_file:
        for line in tweet_file:
            add_record(line.lower(), feature_list, data)


def add_record(tweet, feature_list, dataset):
    record = []
    for feature in feature_list:
        count = 0
        if feature in tweet and look_negative_words(tweet, feature):
            count = 1

        record.append(count)
    data = ",".join(map(str, record))
    data += "\n"

    with open(dataset, 'a') as output_file:
        output_file.write(data)


def look_negative_words(line, feature):
    if feature not in SENTIMENT_LIST:
        return True
    for word in WORDS:
        if word in line:
            return False
    return True


def main():
    create_dataset(FEATURES, TWEETS, VALIDATION_DATA)

if __name__ == '__main__':
    main()
