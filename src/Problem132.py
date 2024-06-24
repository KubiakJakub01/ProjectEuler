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
    primes = []
    n = 10**9
    k = 1
    while len(primes) < 40:
        if pow(10, n, 9 * repunit(k)) == 1:
            if factorint(repunit(k)).keys() == [3]:
                primes.append(repunit(k))
        k += 1
    return sum(primes)


if __name__ == "__main__":
    print(solution())
