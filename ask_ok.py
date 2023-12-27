#!/usr/bin/env python3
""" Example of a function with one or more default argument values
"""


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """Asks ok

    Args:
        prompt (str): Promt text to be displayed
        retries (int): The number of retries. Defaults to 4
        reminder (str): Reminder text. Defaults to 'Please try again'

    Returns:
        bool: True or False

    Raises:
        ValueError: When retries is less than 0

    """
    while True:
        reply = input(prompt)
        """str: reply from the user"""
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("Invalid user response")
        print(reminder)


if __name__ == '__main__':
    ask_ok('Do you really want to quit?')
    ask_ok('Ok to overwrite the file?', 2)
    ask_ok('Ok to overwrite the file?', 2, 'Come on, only yes or no!')
