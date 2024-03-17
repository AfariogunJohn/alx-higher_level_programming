#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    only allows new instance  attribute which is called first_name
    """

    __slots__ = ["first_name"]
