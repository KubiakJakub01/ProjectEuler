"""
Created on 01.05.2024

Problem 130: Composites with Prime Repunit Property
https://projecteuler.net/problem=130

@author: KubiakJakub01

Algorithm description:
    TODO
"""
from collections import deque

from .utils import divisors, pnu, timer

N = 25


def is_divisible(n: str, i: int):
    try:
        return int(n) % i == 0
    except ValueError:
        n_deque = deque(n[::-1])
        p = ""
        while n_deque:
            p += n_deque.pop()
            p = str(int(p) % i)

        if p == "0":
            return True
        return False


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
            repunit = "1" * div
            if is_divisible(repunit, n):
                print(f"{n_results=}: {n=}")
                sum_results += n
                n_results += 1
                break

    print(sum_results)


if __name__ == "__main__":
    solution()


"""
--- 8.679726123809814 seconds ---
"""
