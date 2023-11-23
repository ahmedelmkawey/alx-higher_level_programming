#!/usr/bin/python3
"""
Class Square that defines a square
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
    Args:
        size -> must be integer
    Methods:
        __init__(self, size=0)
        area(self) -> public instance method return area
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculatre square area """
        return(self.__size * self.__size)
