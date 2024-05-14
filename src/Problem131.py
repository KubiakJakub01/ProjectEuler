"""
Created on 04.05.2024

Problem 131: Prime Cube Partnership
https://projecteuler.net/problem=131

@author: KubiakJakub01

Algorithm description:
    1. Generate prime numbers up to N = 10^6.
    2. Initialize the count variable.
    3. Initialize x = 1.
    4. Iterate while True.
    5. Calculate the polynomial function f(x) = 3 * x^2 - 3 * x + 1.
    6. If the value of f(x) is greater or equal to N, break the loop.
    7. If the value of f(x) is a prime number, increment the count variable.
    8. Increment x by 1.
    9. Print the count variable.
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
