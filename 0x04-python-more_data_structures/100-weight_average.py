#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numm = 0
    denn = 0
    for tup in my_list:
        numm += tup[0] * tup[1]
        denn += tup[1]
    return (numm / denn)
