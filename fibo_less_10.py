#!/usr/bin/env python3
# Fibonacci series
# The sum of two numbers defines the next
a, b = 0, 1
while a < 10:
    print(a, end=',')
    a, b = b, a + b
print()
