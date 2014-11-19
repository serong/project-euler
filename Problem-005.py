"""
    Problem 005 - Smallest Multiple
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    2520 is the smallest number that can be divided by each
    of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly
    divisible by all of the numbers from 1 to 20?

    :url:
    https://projecteuler.net/problem=5

    :answer: 232792560
    :time: 0.0005

    :author:
    :updated: 2014-11-18
"""

from tools.prime import return_next_prime
from time import time
t = time()


def factor_count(n, factor):
    """ Check if n is a power of factor, return -1 if not
    else return the power.

        >>> factor_count(8,2)
        3

        >>> factor_count(81, 3)
        4

        >>> factor_count(10,2)
        0

        >>> factor_count(3,2)
        0

        >>> factor_count(2,2)
        1
    """

    count = [0]

    def inner(n, factor):
        result = n / factor
        remainder = n % factor

        if result == 1 and remainder == 0:
            count[0] += 1
            return
        else:
            if remainder > 0:
                count[0] = 0
                return
            else:
                count[0] += 1
                inner(n/factor, factor)

    inner(n, factor)
    return count[0]


def biggest_power(n, alist):
    """ Given a list of numbers :list:alist, find the
        biggest power of n.

        >>> biggest_power(2, [1,2,3,4])
        2

        >>> biggest_power(3, [1,2,3,4,5,6,7,8,9])
        2

        >>> biggest_power(2, [1,2,3,4,5,6,7,8,9,10])
        3
    """
    result = 0

    for num in alist:
        if factor_count(num, n) > 0:
            result += 1
    return result


def smallest_multiple(n):
    """ Smallest multiple of numbers below n.

        >>> smallest_multiple(10)
        2520
    """

    primes = [2]
    while primes[-1] < n:
        prime = return_next_prime(primes)
        primes.append(prime)

    # Checking the last element and the loop.
    if primes[-1] > n:
        del primes[-1]

    # Now we have our primes list. Time to check
    # biggest_powers.

    multiple = 1
    ranged = [x for x in range(1, n+1)]
    for prime in primes:
        power = biggest_power(prime, ranged)
        multiple *= prime**power

    return multiple


print smallest_multiple(20)
print "Finished in: ", time() - t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
