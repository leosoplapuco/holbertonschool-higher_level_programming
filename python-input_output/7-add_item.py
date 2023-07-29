#!/usr/bin/python3
"""module module"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    # Try to load existing data from the file
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty list
    data = []

# Add the command line arguments to the list
data.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(data, "add_item.json")
