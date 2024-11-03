#!/usr/bin/python3
"""
Module for defining the Square class with a private instance attribute.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes the square with a given size."""
        self.__size = size
