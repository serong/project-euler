# -*- coding: utf-8 -*-
"""
    problem 006 - sum square difference
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    the sum of the squares of the first ten natural numbers is,
        12 + 22 + ... + 102 = 385

    the square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)2 = 552 = 3025

    hence the difference between the sum of the squares of the
    first ten natural numbers and the square of the sum is,
        3025 − 385 = 2640.

    find the difference between the sum of the squares of the
    first one hundred natural numbers and the square of the sum.

    :url:
    https://projecteuler.net/problem=6

    :answer: 25164150
    :time: 0.0004

    :author:
    :updated: 2014-11-18
"""

from time import time
t = time()


def sum_square_diff(n):
    """ Return the difference of "sum of the squares" and
        "square of the sums" of the first n natural numbers.

        >>> sum_square_diff(10)
        2640
    """

    numbers = [x for x in range(1, n+1)]
    squares = [x**2 for x in numbers]

    result = abs(sum(squares) - sum(numbers) ** 2)
    
    return result


print sum_square_diff(100)
print "Finished in: ", time() - t

if __name__ == "__main__":
    import doctest
    doctest.testmod()
