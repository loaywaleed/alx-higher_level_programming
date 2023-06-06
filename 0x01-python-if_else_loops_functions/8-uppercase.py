#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            new_string += "{0:c}".format(ord(i) - 32)
        else:
            new_string += i
    print(new_string)
