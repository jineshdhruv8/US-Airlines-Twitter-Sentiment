"""
File: classification.py
Language: Python 3.5.2
Description: Using training set model is created using SVM, Naive Bayes, 
Neural Networks and the model is tested on testing set and validation set.
"""

import csv
import svm_classifier
import naive_bayes_classifier
import neural_networks

TRAINING_DATA = "./dataset/training_data.csv"
TEST_DATA = "./dataset/test_data.csv"
VALIDATION_DATA = "./dataset/validation_data.csv"


def classifier():
    data = []
    target = []
    with open(TRAINING_DATA, encoding="utf-8", newline='') as input_file:
        reader = csv.reader(input_file, delimiter=',', quotechar='|')
        for record in reader:
            row = record[:110]
            row = list(map(int, row))
            data.append(row)
            target.append(record[110])

    test_data = []
    target_result = []
    with open(VALIDATION_DATA, encoding="utf-8", newline='') as input_file:
        reader = csv.reader(input_file, delimiter=',', quotechar='|')
        for record in reader:
            row = record[:110]
            row = list(map(int, row))
            test_data.append(row)
            target_result.append(record[110])

    test_result = svm_classifier.classification(data, target, test_data)
    print("Support vector machine:")
    calculate_accuracy(test_result, target_result)
    test_result = naive_bayes_classifier.classification(data, target, test_data)
    print("Naive Bayes:")
    calculate_accuracy(test_result, target_result)
    print("Neural Networks:")
    neural_networks.neural_networks_classifier(data, target, test_data, target_result, 0.3, 5, 10)


def calculate_accuracy(test_result, target_result):
    match = 0
    total_test_data = len(test_result)
    for i in range(total_test_data):
        if test_result[i] == target_result[i]:
            match += 1

    # print("Total observation: {}    Match: {}".format(total_test_data, match))
    accuracy = (match / total_test_data) * 100
    print("Accuracy: {}".format(accuracy))

if __name__ == '__main__':
    classifier()
