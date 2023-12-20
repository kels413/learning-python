#!/usr/bin/python3
""" class to define square"""


class Square:
    """
    Representation of a square.
    """
    def __init__(self, size=0):
        """
        the init function that gets invoked when a new instance is created
        :param size:
        """

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
       return self.__size **2






"""
Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module
"""
