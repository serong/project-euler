"""
    Problem 002 - Even Fibonacci Numbers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.

    :url:
    https://projecteuler.net/problem=2

    :answer: 4613732

    :author:
    :updated: 2014-11-18
"""


def fibonacci_even_sum(limit):
    """ Return the sum of even fibonacci numbers below
        :arg:limit.

        >>> fibonacci_even_sum(10)
        10

        >>> fibonacci_even_sum(35)
        44
    """

    a, b = 0, 1
    even_sums = 0

    while b < limit:
        a, b = b, a + b
        if b % 2 == 0:
            even_sums += b

    return even_sums


if __name__ == "__main__":
    import doctest
    doctest.testmod()