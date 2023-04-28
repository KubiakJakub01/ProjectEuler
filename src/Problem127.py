"""
Created on 05-01-2023 17:01

Problem 127: abc-hits
https://projecteuler.net/problem=127

author: KubiakJakub01
"""

# import libraries
import time

# import default dictionary
from collections import defaultdict

import numpy as np

# import utils
from utils import prime_number_utils as pnu

MAX_N = 1000

# defaultdict in format
# {key: number -> val: list of prime factors}
number_rad_dict = defaultdict(list)
number_rad_dict[1] = []


# main solution function
def solution():
    result = 0
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

    # define working dicotnary with set of prime factors and rad of all numbers
    number_prime_factor_rad_dict = {
        i: (set(number_rad_dict[i]), np.prod(list(set(number_rad_dict[i]))))
        for i in range(1, MAX_N + 1)
    }
    count = 0
    # print(number_prime_factor_rad_dict)
    # iterate over all numbers
    for number, prime_factor_rad in number_prime_factor_rad_dict.items():
        # delete duplicates
        prime_factor_list = prime_factor_rad[0]
        # define availability list with relatively prime numbers for the current number of
        relatively_prime_list = np.arange(number, MAX_N + 1)
        # remove multiples of all prime factors of the current number
        for prime_factor in prime_factor_list:
            relatively_prime_list = relatively_prime_list[
                relatively_prime_list % prime_factor != 0
            ]
        # iterate over all relatively prime numbers
        for relatively_prime_number in relatively_prime_list:
            # check if sum of relatively prime number and current number is in relatively prime list
            c = number + relatively_prime_number
            if c in relatively_prime_list:
                # print(f"before 4 condition: {number}, {relatively_prime_number}, {c}")
                multiplication = (
                    prime_factor_rad[1]
                    * number_prime_factor_rad_dict[relatively_prime_number][1]
                    * number_prime_factor_rad_dict[c][1]
                )
                # check if multiplication of rad of current number, relatively prime number and c is smaller than c
                if multiplication < c:
                    print(
                        f"{number}({prime_factor_rad[1]}), {relatively_prime_number}({number_prime_factor_rad_dict[relatively_prime_number][1]}), {c}({number_prime_factor_rad_dict[c][1]})"
                    )
                    count += 1
                    result += c

    print(f"Result: {result} with {count} solutions")


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("--- %s seconds ---" % (time.time() - start_time))
