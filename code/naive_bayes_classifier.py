"""
File: naive_bayes_classifier.py
Language: Python 3.5.2
Description: Naive Bayes classification using sklearn 
"""

import numpy
from sklearn.naive_bayes import GaussianNB


def classification(data, target, test_data):
    for row in range(len(data)):
        for column in range(len(data[row])):
            data[row][column] = data[row][column] + 1

    for row in range(len(test_data)):
        for column in range(len(test_data[row])):
            test_data[row][column] = test_data[row][column] + 1

    cls = GaussianNB()
    x = numpy.array(data)
    y = numpy.array(target)
    cls.fit(x, y)
    test = numpy.array(test_data)
    result = cls.predict(test)
    result_list = []
    for element in result:
        result_list.append(element)

    return result_list
