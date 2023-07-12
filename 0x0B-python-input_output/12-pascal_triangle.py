#!/usr/bin/python3
"""module that has pascal_triangle function"""


def pascal_triangle(n):
    """function that returns pascal triangle"""
    if n <= 0:
        return []

    my_list = [[1]]

    for i in range(0, n - 1):
        temp = [0] + my_list[-1] + [0]
        row = []
        for j in range(len(my_list[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        my_list.append(row)

    return my_list
