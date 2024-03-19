#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reps a square."""

    def __init__(self, size):
        """Initializer

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
