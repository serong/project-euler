# -*- coding: utf-8 -*-
"""
    Problem 009 - Special Py. Triangle
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    A Pythagorean triplet is a set of three natural numbers,
    a < b < c, for which,
        a2 + b2 = c2

    For example,
        32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which
    a + b + c = 1000.

    Find the product abc.

    :url:
    https://projecteuler.net/problem=9

    :answer:
    :time:

    :author:
    :updated: 2014-11-19
"""
from time import time
from math import sqrt
t = time()


def sum_squares(a, b):
    """ Sum of squares.

        >>> sum_squares(2, 3)
        13
    """

    return a*a + b*b


def find_c(a, b):
    """ Find the long side of the
        triangle.
    """

    result = sqrt(sum_squares(a, b))
    return result


def find_it(n):
    """ n:1000 in this case.
    """

    # a, b, c should be smaller then
    # half of their sum.
    limit = n / 2
    n = float(n)

    checked = []

    for a in range(1, limit):
        for b in range(1, limit):
            if (a, b) in checked or (b, a) in checked:
                print "Passing: \t", (a, b)
                pass
            else:
                print "Checking: \t", (a, b)
                checked.append((a, b))
                c = find_c(a, b)
                if c.is_integer():
                    total = a + b + c
                    if total == n:
                        found = (a, b, c)
                        print "c : ", c, " - ", a + b + c
                        break
    print found


find_it(1000)
print "Finished in:", time() - t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
