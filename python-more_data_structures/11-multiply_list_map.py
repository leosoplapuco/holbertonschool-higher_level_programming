#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

print(roman_to_int("XXIV"))

values = [1, 2, 3, 4, 5]
multiplied_values = multiply_list_map(values, 3)
print(multiplied_values)
