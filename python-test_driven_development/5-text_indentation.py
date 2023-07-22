#!/usr/bin/python3
""" module test_indentation """

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_split = [".", "?", ":"]
    lines = []
    line = ""
    for char in text:
        line += char
        if char in chars_to_split:
            lines.append(line.strip())
            line = ""
    if line:
        lines.append(line.strip())

    print("\n\n".join(lines))
