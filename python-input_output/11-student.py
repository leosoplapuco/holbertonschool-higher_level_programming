#!/usr/bin/python3
"""module Student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    json_dict[attr] = self.__dict__[attr]
            return json_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
