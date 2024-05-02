"""
Created on 01.05.2024

Problem 130: Composites with Prime Repunit Property
https://projecteuler.net/problem=130

@author: KubiakJakub01

Algorithm description:
    TODO
"""
from .utils import divisors, pnu, timer

N = 25


@timer
def solution():
    sum_results = 0
    n_results = 0
    n = 7

    while n_results < N:
        n += 2
        if pnu.is_prime(n) or n % 5 == 0:
            continue

        n_1 = n - 1
        for div in divisors(n_1):
            repunit = int("1" * div)
            if repunit % n == 0:
                print(f"{n=}")
                sum_results += n
                n_results += 1
                break

    print(sum_results)


if __name__ == "__main__":
    solution()
