# -*- coding: utf-8 -*-
"""
    Problem 010 - Summation of Primes
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    The sum of the primes below 10 is:
        2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

    :url:
    https://projecteuler.net/problem=10

    :answer: 142913828922
    :time: 14.5s

    :note:
    I've used a fast prime algorithms found at Wikibooks.
    My original solution to finding primes, while working okay,
    was quite slow. The algorithm and its details can be
    found at '/tools' folder.

    :author:
    :updated: 2014-11-19
"""

from time import time
from tools import fast_prime as fsp
t = time()

primes = fsp.fast_prime(2000000)
print sum(primes)
print "Finished in: ", time() - t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
