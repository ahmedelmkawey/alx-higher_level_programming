#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    def __init__(self, size=0):
        """
         Args:
            size: size of the square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """square value"""
        return (self.__size**2)
