"""
Created on 16.05.2024

Problem 132: Large Repunit Factors
https://projecteuler.net/problem=132

Algorithm description:
    TODO: Write the algorithm description.

@author: KubiakJakub01
"""

from .utils import timer

from sympy.ntheory import factorint


def repunit(k):
    return (10**k - 1) // 9


@timer
def solution():
    R_10_9 = repunit(10**9)
    factors = factorint(R_10_9)
    primes = sorted(factors.keys())
    first_40_primes = primes[:40]
    sum_first_40_primes = sum(first_40_primes)

    return sum_first_40_primes


if __name__ == "__main__":
    # Get the sum
    sum_of_first_40_primes = solution()
    print(
        "The sum of the first 40 prime factors of R(10^9) is:", sum_of_first_40_primes
    )
