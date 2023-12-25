#!/usr/bin/env python3
# Prime numbers less than n
end = int(input("Enter a whole nuber greater than 1: "))
for n in range(2, end):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
