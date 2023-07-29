#!/usr/bin/python3
class Person:
    """class Person"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

person = Person("John", 30, True)
json_dict = class_to_json(person)
print(json_dict)
