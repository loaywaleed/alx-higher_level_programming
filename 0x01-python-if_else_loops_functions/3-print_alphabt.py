#!/usr/bin/python3
for i in range(97, 123):
    if "{0:c}".format(i) != "q" and "{0:c}".format(i) != "e":
        print("{0:c}".format(i), end='')
