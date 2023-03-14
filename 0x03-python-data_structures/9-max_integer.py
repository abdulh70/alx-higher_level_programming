#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for b in range(len(my_list)):
            if my_list[b] > max:
                max = my_list[b]
        return max
