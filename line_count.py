#!/usr/bin/env python3
""" File line count

This program displays the number of lines in each file passed as a command
line argument

"""
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('Cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
