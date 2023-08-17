#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list is not None:
        average_grades = 0
        sum_of_weights = 0
        for items in my_list:
            average_grades += (items[0] * items[1])
            sum_of_weights += items[-1]

        return (average_grades / sum_of_weights)
    else:
        return 0
