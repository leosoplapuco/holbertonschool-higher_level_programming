#!/usr/bin/python3
"""module read_file"""


def read_file(filename=""):
    """function read_file"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
