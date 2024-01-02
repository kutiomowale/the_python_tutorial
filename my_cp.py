#!/usr/bin/env python3
"""A minimal version of linux cp command


Example:
    ./my_cp.py file1 file2
This makes a copy of file1 as file2

I implemented file copying, not directory copying

"""


def my_cp():
    try:
        import sys
        args = sys.argv
        if len(args) != 3:
            print("Usage: ./my_cp.py file1 file2")
            return

        with open(f'{args[1]}', 'r', encoding='utf-8') as f1:
            text = f1.read()

        with open(f'{args[2]}', 'w', encoding='utf-8') as f2:
            f2.write(text)
    except Exception as e:
        print(e)


my_cp()
