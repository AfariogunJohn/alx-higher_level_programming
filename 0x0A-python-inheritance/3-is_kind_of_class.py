#!/usr/bin/python3
"""a function thatchecks for instaces"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class

    Args:
        obj: The object to check.
        a_class: The class to check against.
    """
    return (isinstance(obj, a_class))