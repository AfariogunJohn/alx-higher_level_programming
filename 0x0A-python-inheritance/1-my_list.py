#!/usr/bin/python3
""" a class that inherits list"""


class MyList(list):
    """a inheritor of list"""
    def __init__(self):
        """initializer"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
