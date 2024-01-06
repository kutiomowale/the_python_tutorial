#!/usr/bin/env python3
import doctest
"""This module is for the doctest and unittest example.

average computes arithmetic of a list of numbers.


"""


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    Args:
        values (list): List of numbers

    Returns:
        int: The average of values
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()
