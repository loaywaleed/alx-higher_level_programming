#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
            'X': 10,
            'V': 5,
            'I': 1,
            'C': 100,
            'L': 50,
            'D': 500,
            'M': 1000
            }
    if not roman_string or type(roman_string) != str:
        return 0
    after_conv = 0
    for i in range(len(roman_string)):
        for j in roman_dict:
            if j == roman_string[i]:
                if i > 0 and roman_dict[j] > roman_dict[roman_string[i - 1]]:
                    after_conv = roman_dict[j] - after_conv
                else:
                    after_conv += roman_dict[j]
    return after_conv
