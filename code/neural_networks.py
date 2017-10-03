"""
File: neural_networks.py
Language: Python 3.5.2
Description: Using training data set creates a model using backward propagation and
predicts the results.
Reference: How to Implement the Backpropagation Algorithm From Scratch In Python. Jason Brownlee.
http://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/
"""
from random import seed
from random import random
import math
import data_setup_neural_network


seed(0.2)


def init(number_of_input, number_of_hidden, number_of_output):
    hidden_layer = [{'weights': [random() for r in range(number_of_input+1)]}
                    for r in range(number_of_hidden)]
    output_layer = [{'weights': [random() for r in range(number_of_hidden+1)]}
                    for r in range(number_of_output)]
    network = [hidden_layer, output_layer]
    return network


def calculate_activation(weight, inputs):
        length = len(weight)-1
        bias = weight[length]
        actn = 0
        for count in range(length):
            actn += weight[count] * inputs[count]
        return actn + bias


def transfer_neuron_activation(actn):
    return 1/(1+math.exp(-actn))


def forward_propagation(network, observation):
    inputs = observation
    for layer in network:
        next_input = []
        for neuron in layer:
            actn = calculate_activation(neuron['weights'], inputs)
            neuron['result'] = transfer_neuron_activation(actn)
            next_input.append(neuron['result'])
        inputs = next_input
    return inputs


def error_back_propagation(network, expected):
    length = len(network)
    for count in range(length-1,-1,-1):
        layer = network[count]
        error = []
        if count == length-1:
            for i in range(len(layer)):
                neuron = layer[i]
                error.append(expected[i] - neuron['result'])
        else:
            for i in range(len(layer)):
                err = 0
                for neuron in network[count+1]:
                    err += neuron['weights'][i] * neuron['delta']
                error.append(err)
        for i in range(len(layer)):
            neuron = layer[i]
            output = neuron['result']
            neuron['delta'] = error[i] * (output * (1-output))


def update_weight(network, observation, learning_rate):
    length = len(observation)
    for count in range(len(network)):
        inpt = observation[:length-1]
        if count != 0:
            inpt = [neuron['result'] for neuron in network[count - 1]]
        for neuron in network[count]:
            for i in range(len(inpt)):
                neuron['weights'][i] += learning_rate * neuron['delta'] * inpt[i]
            neuron['weights'][-1] += learning_rate * neuron['delta']


def training(network, observations, learning_rate, epoch_count, outputs):
    for epoch in range(epoch_count):
        error = 0
        for observation in observations:
            output = forward_propagation(network, observation)
            expected = [0 for x in range(outputs)]
            expected[observation[-1]] = 1
            error += sum([(expected[i] - output[i])**2 for i in range(len(expected))])
            error_back_propagation(network, expected)
            update_weight(network, observation, learning_rate)



def predict(network, observation):
    output = forward_propagation(network, observation)
    return output.index(max(output))


def neural_networks_classifier(training_set, training_result, testing_set, testing_result, learning_rate,
                               epochs, number_of_hidden):
 
    number_of_input = len(training_set[0])-1
    number_of_output = len(set(x for x in training_result))
    training_data, testing_data = data_setup_neural_network.convert_target_class(training_set, training_result,
                                                                                 testing_set, testing_result)
    network = init(number_of_input, number_of_hidden, number_of_output)
    training(network, training_data, learning_rate, epochs, number_of_output)
    results = []
    for observation in testing_data:
        result = predict(network, observation)
        results.append(result)

    evaluate_result(results, testing_data)


def evaluate_result(results, testing_results):
    total_match = 0
    length = len(results)
    size = len(testing_results[0])
    for count in range(length):
        if results[count] == testing_results[count][size-1]:
            total_match += 1

    accuracy = (total_match/length) * 100
    print("Accuracy: {}%".format(accuracy))

