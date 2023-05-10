#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
sentence = f"Last digit of {number:d} is {last_digit:d}"
if last_digit > 5:
    print(sentence + " and is greater than 5")
elif last_digit == 0:
    print(sentence + " and is 0")
elif last_digit < 6:
    print(sentence + " and is less than 5 and not 0")
