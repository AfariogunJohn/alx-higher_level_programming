#!/usr/bin/python3
"""A class called rectangle, with some attributes"""


class Rectangle:
    """a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a new rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            rect += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """returns an official representation of the class"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """returns a string upon deletion of an instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        compares two instances of Rectangle by area and returns the larger
        Args:
            rect_2: rectangle 2
            rect_1: rectangle 1
        Raises:
            TypeError, if not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
