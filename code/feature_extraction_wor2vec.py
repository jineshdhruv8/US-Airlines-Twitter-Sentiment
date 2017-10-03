"""
File: feature_extraction_word2vec.py
Language: Python 3.5.2
Description: Using the given attributes finds the most similar words
present in the file.
"""
from gensim.models import word2vec


TWEET = "./cleaned_data"
NEGATIVE_TWEETS = "./data/negative_tweets"
POSITIVE_TWEETS = "./data/positive_tweets"
NEUTRAL_TWEETS = "./data/neutral_tweets"
FEATURE = "./inputs/features"


def get_similar_feature(data, feature_list):
    sentences = word2vec.Text8Corpus(data)
    model = word2vec.Word2Vec(sentences, size=200)
    for feature in feature_list:
        try:
            print(model.most_similar([feature]))
        except KeyError:
            pass


def get_feature():
    feature = []
    with open(FEATURE, encoding='utf-8') as input_file:
        for line in input_file:
            feature.append(line.strip())

    return feature


if __name__ == '__main__':
    features = get_feature()
    get_similar_feature(POSITIVE_TWEETS, features)
    get_similar_feature(NEGATIVE_TWEETS, features)
    get_similar_feature(NEGATIVE_TWEETS, features)
