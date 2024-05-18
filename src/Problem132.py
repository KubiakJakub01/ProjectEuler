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


def prime_factors_of_repunit(primes, limit=40):
    factors = []
    k = 10**9
    repunit_modulus = (10**k - 1) // 9

    for prime in primes:
        while repunit_modulus % prime == 0:
            factors.append(prime)
            repunit_modulus //= prime
            if len(factors) >= limit:
                return factors

    return factors


def repunit_length_k(k):
    return (10**k - 1) // 9


@timer
def solution():
    primes = pnu.eratos(N)

    factors = []
    current_number = 10**9
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
