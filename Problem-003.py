"""
    Problem 003 - Largest Prime Factor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    :url:
    https://projecteuler.net/problem=3

    :answer: 6857
    :time: 2.1s

    :author:
    :updated: 2014-11-18
"""


def largest_prime(n):
    """ Return the largest prime factor of a number.

        >>> largest_prime(13195)
        29

        >>> largest_prime(15)
        5
    """

    primes = [2]

    while True:
        if n == 1:
            break
        while n % primes[-1] == 0:
            n = n / primes[-1]
        np = return_next_prime(primes)
        if n != 1:
            primes.append(np)

    return max(primes)


def return_next_prime(previous):
    """ Given a starting point (a list) return the next prime
        number.

        >>> return_next_prime([2,3,5,7])
        11

        >>> return_next_prime([2,3,5,7,11])
        13
    """

    candidate = max(previous) + 1

    while True:
        checks = []
        for number in previous:
            checks.append(candidate % number == 0)
        if True not in checks:
            break
        else:
            candidate += 1

    return candidate


if __name__ == "__main__":
    import doctest
    doctest.testmod()
