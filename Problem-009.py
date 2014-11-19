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

    :answer: 31875000
    :time: 0.3s

    :author:
    :updated: 2014-11-19
"""
from time import time
t = time()


def sroot(n):
    """ Check if n's square root is a real number.

        >>> sroot(25)
        True

        >>> sroot(26)
        False
    """

    return int(n ** 0.5) == n ** 0.5


def find_it():
    """ Find a, b, c where:
        a + b + c = 1000
    """

    # It's unlikely of a, b, c to be higher
    # than 1000/2
    limit = 500

    found = ()

    i = 1
    while i < limit:
        j = 1
        while j < limit:
            k = find_k(i, j)
            if i + j + k == 1000:
                found = (i, j, k)
            j += 1
        i += 1

    product = 1

    for number in found:
        product *= number

    return int(product)


def find_k(i, j):
    """ Find the long side of the
        triangle.
    """

    result = ((i * i) + (j * j)) ** 0.5
    return result


print find_it()
print "Finished in:", time() - t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
