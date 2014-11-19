"""
    Problem 001 - Multiples of 3 and 5
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    If we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    :url:
    https://projecteuler.net/problem=1

    :answer: 233168

    :author:
    :updated: 2014-11-18
"""


def sum_divisibles(limit):
    """ Sum the numbers below limit that are divisible by
        3 or 5.

        >>> sum_divisibles(10)
        23
    """
    res = [x for x in range(limit) if x % 3 == 0 or x % 5 == 0]
    return sum(res)


def sum_divisibles_lambda(limit):
    """ Sum the numbers below limit that are divisible by
        3 or 5.

        >>> sum_divisibles_lambda(10)
        23
    """
    f = lambda x: x % 3 == 0 or x % 5 == 0
    ls = [x for x in range(limit) if f(x)]

    return sum(ls)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
