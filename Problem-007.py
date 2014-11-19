# -*- coding: utf-8 -*-
"""
    Problem 007 - 10001st Prime
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?

    :url:
    https://projecteuler.net/problem=7

    :answer: 104743
    :time: 173s

    :author:
    :updated: 2014-11-18
"""

from time import time
from tools.prime import return_next_prime
t = time()


def prime_n(n):
    """ Return the nth prime.

        >>> prime_n(3)
        5

        >>> prime_n(6)
        13
    """

    primes = [2]
    while len(primes) != n:
        next_p = return_next_prime(primes)
        primes.append(next_p)

    return primes[-1]


print prime_n(10001)
print "Finished in: ", time() - t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
