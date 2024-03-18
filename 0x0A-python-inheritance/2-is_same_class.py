#!/usr/bin/python3
"""a function thatchecks for instaces"""


def is_same_class(obj, a_class):
    """a function that checks if an object is of the same type as a class
    Args:
        obj: the object
        a_class: the class to check against
    """
    return type(obj) is a_class
