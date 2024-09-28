"""
Created on 16.05.2024

Problem 132: Large Repunit Factors
https://projecteuler.net/problem=132

Algorithm description:
    TODO: Write the algorithm description.

@author: KubiakJakub01
"""

from .utils import timer


def repunit(k):
    return (10**k - 1) // 9


@timer
def solution():
    n = 10**9
    prime_factors = []
    for p in range(2, n):
        if 10**n % p == 1:
            prime_factors.append(p)
        if len(prime_factors) == 40:
            break
    return sum(prime_factors)


if __name__ == "__main__":
    print(solution())
