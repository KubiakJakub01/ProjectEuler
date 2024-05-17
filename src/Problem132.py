"""
Created on 16.05.2024

Problem 132: Large Repunit Factors
https://projecteuler.net/problem=132

Algorithm description:
    TODO: Write the algorithm description.

@author: KubiakJakub01
"""

from .utils import timer, pnu

N = 10**6
K = 10**9


def prime_factors(n, primes):
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
            if len(factors) >= 40:
                return factors
        if prime * prime > n:
            break
    if n > 1:
        factors.append(n)
    return factors


def repunit_length_k(k):
    return (10**k - 1) // 9


@timer
def solution():
    primes = pnu.eratos(N)

    factors = []
    current_number = (
        10**9
    )  # Since we use R(10^9) as (10^10^9 - 1) / 9, we just use 10^9 here
    for prime in primes:
        if len(factors) >= 40:
            break
        while current_number % prime == 0:
            factors.append(prime)
            current_number //= prime
            if len(factors) >= 40:
                break

    sum_of_prime_factors = sum(factors[:40])

    print(sum_of_prime_factors)


if __name__ == "__main__":
    solution()
