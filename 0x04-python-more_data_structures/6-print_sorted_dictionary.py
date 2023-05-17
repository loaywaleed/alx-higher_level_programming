#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary)
    for i in sort_dict:
        print("{:s}: {}".format(i, a_dictionary[i]))
