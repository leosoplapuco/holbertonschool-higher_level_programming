#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is None or isinstance(value, set):
            raise TypeError("Invalid value")
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
