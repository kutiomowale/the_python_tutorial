#!/usr/bin/env python3
# Examples of using match statements in python
# point is an (x, y) tuple
def where_am_i(point):
    match point:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f'Y={y}')
        case (x, 0):
            print(f'X={x}')
        case (x, y):
            print(f'X={x}, Y={y}')
        case _:
            print('Not a point')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print('Origin')
        case Point(x=0, y=y):
            print(f'Y={y}')
        case Point(x=x, y=0):
            print(f'X={x}')
        case Point(x=x, y=y):
            print(f'X={x}, Y={y}')
        case Point():
            print('Somewhere else')
        case _:
            print('Not a point')


if __name__ == '__main__':
    where_am_i((0, 0))
    where_am_i((5, 0))
    where_am_i((0, 5))
    where_am_i((3, 9))
    where_am_i(6)

    print("***********")

    where_is(Point(0, 0))
    where_is(Point(5, 0))
    where_is(Point(0, 5))
    where_is(Point(3, 9))
    where_is(6)
