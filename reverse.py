#!/usr/bin/env python3
import doctest


class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def reverse(data):
    """A Generator to loop backwards

    Creates an iterator for looping over a sequence backwards

    Args:
        data (sequence): Any sequence

    Yields:
        Successive elements in reverse order

    Examples:
        >>> for char in reverse('golf'):
        ...     print(char)
        f
        l
        o
        g
    """
    for index in range(len(data)-1, -1, -1):
        yield data[index]


if __name__ == '__main__':
    doctest.testmod()
