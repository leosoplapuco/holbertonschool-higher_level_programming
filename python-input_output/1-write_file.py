#!/usr/bin/python3
"""module write_file"""


def write_file(filename="", text=""):
    """function write_file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
