"""
    Problem 004 - Largest Palindrome Product
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is: 9009 -- 91 and 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    :url:
    https://projecteuler.net/problem=4

    :answer: 906609
    :time: 1.8s

    :author:
    :updated: 2014-11-18
"""


def is_palindrome(arg):
    """ Check if a number or a string is palindrome.

        >>> is_palindrome("abba")
        True

        >>> is_palindrome(12321)
        True

        >>> is_palindrome("abcbd")
        False

        >>> is_palindrome("abbc")
        False
    """

    arg = str(arg)

    return arg == arg[::-1]


def largest_palindrome():
    """ Largest palindrome number made from 3-digit
        numbers.
    """

    results = []
    numbers = [x for x in xrange(100, 1000)]

    for num_a in numbers:
        for num_b in numbers:
            res = num_a * num_b
            if is_palindrome(res):
                results.append(res)

    return max(results)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
