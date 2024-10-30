#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Try to format and print the value as an integer
        return True  # Return True if it worked without error
    except (ValueError, TypeError):
        return False  # Return False if formatting fails

