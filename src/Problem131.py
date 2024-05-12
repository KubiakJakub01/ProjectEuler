"""
Created on 04.05.2024

Problem 130: Prime Cube Partnership
https://projecteuler.net/problem=131

@author: KubiakJakub01

Algorithm description:
    TODO
"""
from .utils import pnu, timer

N = 10**6


def f(x):
    return 3 * x**2 - 3 * x + 1


@timer
def solution():
    primes = pnu.eratos(N)
    count = 0
    x = 1

    while True:
        p = f(x)
        if p >= N:
            break
        if p in primes:
            count += 1
        x += 1

    print(count)


if __name__ == "__main__":
    solution()


"""
--- 0.34201812744140625 seconds ---
"""
