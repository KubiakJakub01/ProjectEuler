# -*- coding: utf-8 -*-
"""
Created on 02-01-2023 17:26

Problem 124: Ordered radicals
https://projecteuler.net/problem=124

@author: Jakub

Algoritm description:
    1. Create a list of all prime numbers up to MAX_N using Eratosthenes sieve
    2. Iterate over nested loop: from 2 to MAX_N and for all prime numbers
    3. Divide number by prime number and add prime number to list of prime factors
    4. If obtained number is in dictionary, add their prime factors current prime factors list
    5. Get rad of all numbers by multiplying all prime factors using set to remove duplicates
    6. Sort rad_dict by rad
    7. Get Kth element
    8. END
"""

# import libraries
import time

# import default dictionary
from collections import defaultdict

import numpy as np

# import utils
from utils import prime_number_utils as pnu

# Constants
MAX_N = 100000
K = 10000

# defaultdict in format
# {key: number -> val: list of prime factors}
number_rad_dict = defaultdict(list)
number_rad_dict[1] = [1]


# main solution function
def solution():
    # get primes up to MAX_N
    primes = pnu.eratos(MAX_N)

    # get prime factors of all numbers
    for num in range(2, MAX_N + 1):
        i = num
        for prime in primes:
            if num % prime == 0:
                num = num // prime
                number_rad_dict[i].append(prime)
                if num in number_rad_dict:
                    number_rad_dict[i].extend(number_rad_dict[num])
                    break

    # get rad of all numbers
    rad_dict = {i: np.prod(list(set(number_rad_dict[i]))) for i in range(1, MAX_N + 1)}

    # sort rad_dict by rad
    sorted_rad_dict = {
        k: v for k, v in sorted(rad_dict.items(), key=lambda item: item[1])
    }

    # get 10000th element
    print(list(sorted_rad_dict.items())[K - 1])


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("--- %s seconds ---" % (time.time() - start_time))

"""
--- 6.523653507232666 seconds ---
"""
