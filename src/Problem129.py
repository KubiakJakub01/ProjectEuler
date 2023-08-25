"""
Created on 15-08-2023

Problem 129: Repunit Divisibility
https://projecteuler.net/problem=129

@author: KubiakJakub01
"""
import time

from .utils.timer import timer

def A(n):
    # Return the smallest number k such that R(k) is divisible by n
    k = 1
    R = 1
    while R != 0:
        R = (R * 10 + 1) % n
        k += 1
    return k

@timer
def solution():
    # Find the least value of n for which A(n) first exceeds 10^6
    n = 10**6
    i = n + 1
    while A(i) <= n:
        i += 2
        while i % 5 == 0:
            i += 2
    return i


if __name__ == "__main__":
    solution()

"""
--- 0.5236790180206299 seconds ---
"""
