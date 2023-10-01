#!/usr/bin/python3
"""Script that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for element in list_of_integers:
        if element > peak:
            peak = element
    return peak
