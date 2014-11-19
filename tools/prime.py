"""
    Prime tools
    ~~~~~~~~~~~

    :desc:
    Some functions that I've been using while solving Euler problems.
"""
import time

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


def siever(n, sieve):
    """ Take a sieve and mark multiplies of
        n False
    """

    result = sieve[:]

    for i in range(2, len(result)):
        if i != n and i % n == 0:
            result[i] = False

    return result


def prime_sieve(n):
    """ Return a list of primes below n.
    """

    sieve = [True for x in range(n)]
    sieve[0], sieve[1] = False, False

    for i in range(2, n):
        sieve = siever(i, sieve)

    primes = []
    for ind, prime in enumerate(sieve):
        if prime is True:
            primes.append(ind)

    return primes
