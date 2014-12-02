# -*- coding: utf-8 -*-
"""
    Problem 012 - Highly Divisible Triangular Number
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:

    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be:
        1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

    The first ten terms would be:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five
    hundred divisors?

    :url:
    https://projecteuler.net/problem=12

    :answer: 76576500
    :time: 9.5s

    :author:
    :updated: 2014-12-02
"""

from time import time
t = time()


def find_divisors(n):
    """ Find all the numbers that divide
        the number n.

        >>> find_divisors(28)
        (6, [1, 2, 4, 7, 14, 28])
    """

    # The upper limit to look for divisors.
    limit = int(n ** 0.5) + 1
    divisors = set()

    for i in range(1, limit):
        divisors.add(n)
        if n % i == 0:
            divisors.add(i)
            x = n / i
            divisors.add(x)

    # So that the list is ordered.
    divisors = list(divisors)
    divisors.sort()
    return len(divisors), divisors


def find_next_triangle_number(previous, index):
    """ Find the next triangle number using the
        previous one and its index.

        >>> find_next_triangle_number(0, 0)
        1

        >>> find_next_triangle_number(6, 3)
        10
    """

    return previous + index + 1


def solve_it(limit):
    """ Solve the problem.

        >>> solve_it(5)
        28
    """
    result = None

    loop = True
    init = 0
    init_ind = 0
    limit = limit

    while loop:
        triangle = find_next_triangle_number(init, init_ind)
        triangle_divisors = find_divisors(triangle)
        if triangle_divisors[0] > limit:
            result = triangle
            loop = False
        init = triangle
        init_ind += 1

    return result


print solve_it(500)
print "Finished in: ", time() - t