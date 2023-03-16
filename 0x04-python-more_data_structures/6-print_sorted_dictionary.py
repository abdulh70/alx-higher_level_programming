#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listt = list(a_dictionary.keys())
    listt.sort()
    for k in list_ord:
        print("{}: {}".format(k, a_dictionary.get(k)))
