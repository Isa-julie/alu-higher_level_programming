#!/usr/bin/python3
"""
Module for defining the Square class with size validation.
"""


class Square:
    """Represents a square with a private size attribute."""
    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Args:
            size (int): The size of the square's side (default is 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  
