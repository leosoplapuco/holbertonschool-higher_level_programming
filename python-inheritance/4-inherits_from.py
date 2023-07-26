#!/usr/bin/python3
"""module inherits_form"""


def inherits_from(obj, a_class):
    """class inherits_form"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
