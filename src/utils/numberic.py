import math
from typing import Generator


def generate_powers(n: int) -> Generator:
    """Create a list of powers of 2 where the sum of last two numbers is less than N"""
    sum_last_two = 0
    i = 1
    while sum_last_two < n:
        power = i**2
        i += 1
        sum_last_two = power + i**2
        yield power


def divisors(n) -> list[int]:
    divs = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, int(n / i)])
    return list(set(divs))
