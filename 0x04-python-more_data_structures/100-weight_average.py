#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = sum(score * weight for score, weight in my_list)
    y = sum(weight for _, weight in my_list)

    return x / y if y != 0 else 0
