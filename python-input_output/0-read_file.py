#!/usr/bin/python3

"""
This module provides a function to read a UTF-8 encoded text file
and print its contents to stdout.
"""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
