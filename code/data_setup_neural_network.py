
POSITIVE = "Positive"
NEUTRAL = "Neutral"
NEGATIVE = "Negative"


def convert(target):
    result = []
    for value in target:
        if value == POSITIVE:
            result.append(1)
        if value == NEUTRAL:
            result.append(2)
        if value == NEGATIVE:
            result.append(0)

    return result


def convert_target_class(training_data, training_target, testing_data, testing_target):
    for row in range(len(training_data)):
        for column in range(len(training_data[row])):
            training_data[row][column] = training_data[row][column] + 1

    for row in range(len(testing_data)):
        for column in range(len(testing_data[row])):
            testing_data[row][column] = testing_data[row][column] + 1

    result = convert(training_target)
    training_set = []
    for count in range(len(training_target)):
        record = training_data[count] + [result[count]]
        training_set.append(record)

    result = convert(testing_target)
    testing_set = []
    for count in range(len(testing_target)):
        record = testing_data[count] + [result[count]]
        testing_set.append(record)

    return training_set, testing_set

