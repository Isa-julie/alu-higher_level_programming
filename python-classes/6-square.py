#!/usr/bin/python3
"""
Defines a Square class with size and position attributes.
"""


class Square:
    """Represents a square with size, position, and print ability."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with size and position.

        Args:
            size (int): Size of the square's side (default 0).
            position (tuple): Position for the square (default (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): New size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position with validation.

        Args:
            value (tuple): Position for the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
              raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#'.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
