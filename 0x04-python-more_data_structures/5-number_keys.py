#!/usr/bin/python3
def number_keys(a_dictionary):
    numz = 0
    list_keys = list(a_dictionary.keys())
    for k in list_keys:
        numz += 1
    return (numz)
