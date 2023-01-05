"""
Utility functions for prime numbers
"""
import numpy as np


def is_prime(n):
    """Return True if n is prime, False otherwise"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True

def enumerate_primes(n):
    """Return a list of prime numbers less than n"""
    return [x for x in range(n) if is_prime(x)]

def eratos(n):
    """Return a list of prime numbers less than n"""
    # Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    # https://www.youtube.com/watch?v=eKp56OLhoQs
    if n < 2:
        return []
    if n == 2:
        return [2]
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True] * n
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n) if prime[p]]

def prime_factors(n):
    """Return a list of prime factors of n"""
    # https://en.wikipedia.org/wiki/Prime_factor
    # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
    # https://www.youtube.com/watch?v=3QnQOYxqRqg
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + prime_factors(n // 2)
    k = 3
    while k * k <= n:
        if n % k == 0:
            return [k] + prime_factors(n // k)
        k += 2
    return [n]

def get_rad(n):
    """Return the rad of n"""
    # https://en.wikipedia.org/wiki/Radical_of_an_integer
    # https://www.geeksforgeeks.org/radical-of-an-integer/
    # https://www.youtube.com/watch?v=3QnQOYxqRqg
    return np.prod(list(set(prime_factors(n))))
