#!/usr/bin/python3
"""module load_form_json_file"""


import json


def load_from_json_file(filename):
    """function load_form_json_file"""
    with open(filename, 'r') as file:
        return json.load(file)
