#!/usr/bin/python3
"""Defines a function for checking inheritance."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object
        a_class (type): The class
    Returns:
        bool (True or False)
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
