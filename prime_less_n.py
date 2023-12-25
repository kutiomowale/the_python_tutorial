#!/usr/bin/env python3
""" Prime numbers less than n

This program asks a user for a number greater than 2, then it displays numbers
less than it indicating those that are prime numbers

It assumes the user would only input a whole number, so no error checking

Example:
    $ ./prime_less_n.py
    Enter a whole number greater than 1: 5
    2 is a prime number
    3 is a prime number
    4 equals 2 * 2

"""

end = int(input("Enter a whole number greater than 1: "))
"""int: User input, prime numbers less than it are displayed"""
for n in range(2, end):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
