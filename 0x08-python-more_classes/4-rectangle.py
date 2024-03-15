#!/usr/bin/python3
"""A class called rectangle, with some attributes"""


class Rectangle:
    """a rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize a new rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns pictorial representation of the rectanfle using #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """returns an official representation of the class"""
        return f"Rectangle({self.__width}, {self.__height})"
