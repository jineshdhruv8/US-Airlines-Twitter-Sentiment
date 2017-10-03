"""
File: svm_classifier.py
Language: Python 3.5.2
Description: Support Vector Machine classification using sklearn 
"""

import numpy
from sklearn import svm


def classification(data, target, test_data):
    cls = svm.SVC()
    x = numpy.array(data)
    y = numpy.array(target)
    cls.fit(x, y)
    test = numpy.array(test_data)
    result = cls.predict(test)
    result_list = []
    for element in result:
        result_list.append(element)
    return result_list
