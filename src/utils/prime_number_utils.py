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


def get_rad_dict(n):
    """Return a dictionary of rad values for all numbers less than n"""
    # https://en.wikipedia.org/wiki/Radical_of_an_integer
    # https://www.geeksforgeeks.org/radical-of-an-integer/
    # https://www.youtube.com/watch?v=3QnQOYxqRqg
    rad_dict = {1: 1}
    for i in range(2, n):
        rad_dict[i] = get_rad(i)
    return rad_dict


def get_rad_list(n):
    """Return a list of rad values for all numbers less than n"""
    # https://en.wikipedia.org/wiki/Radical_of_an_integer
    # https://www.geeksforgeeks.org/radical-of-an-integer/
    # https://www.youtube.com/watch?v=3QnQOYxqRqg
    rad_list = [1]
    for i in range(2, n):
        rad_list.append(get_rad(i))
    return rad_list


def get_totient(n):
    """Return the totient of n"""
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 2 * get_totient(n // 2)
    k = 3
    while k * k <= n:
        if n % k == 0:
            return (k - 1) * get_totient(n // k)
        k += 2
    return n - 1


def get_totient_dict(n):
    """Return a dictionary of totient values for all numbers less than n"""
    totient_dict = {1: 1}
    for i in range(2, n):
        totient_dict[i] = get_totient(i)
    return totient_dict


def get_totient_list(n):
    """Return a list of totient values for all numbers less than n"""
    totient_list = [1]
    for i in range(2, n):
        totient_list.append(get_totient(i))
    return totient_list


def get_totient_sum(n):
    """Return the sum of totient values for all numbers less than n"""
    return sum(get_totient_list(n))


def get_totient_sum_dict(n):
    """Return a dictionary of the sum of totient values for all numbers less than n"""
    totient_sum_dict = {1: 1}
    for i in range(2, n):
        totient_sum_dict[i] = sum(get_totient_list(i))
    return totient_sum_dict


def get_totient_sum_list(n):
    """Return a list of the sum of totient values for all numbers less than n"""
    totient_sum_list = [1]
    for i in range(2, n):
        totient_sum_list.append(sum(get_totient_list(i)))
    return totient_sum_list


def get_totient_sum_matrix(n):
    """Return a matrix of the sum of totient values for all numbers less than n"""
    totient_sum_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            totient_sum_matrix[i, j] = get_totient_sum(i)
            totient_sum_matrix[j, i] = totient_sum_matrix[i, j]
    return totient_sum_matrix
