# -*- coding: utf-8 -*-
"""
Created on 22-09-2022 21:52

Problem 111: Primes with runs
https://projecteuler.net/problem=111

Algoritm description [draft]:
    1. Found all primes numbers below sqrt(10^10) using Sieve of Eratosthenes
    2. Define all possible numbers where: 
        - one digit d occurs n times for n in (8,9,10) and d in (0,1,...,9)
        - other digits occur 10-n times
    3. Make a list of all possible combinations of those numbers
    4. Check which numbers are primes using list of primes from step 1
"""

# import libraries
import time
from collections import defaultdict, Counter
from itertools import permutations, combinations_with_replacement

n = 10
N = 10**11

# Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


# function to define possible arragements of numbers
def define_numbers():
    all_possible_numbers = []
    template_number = ["x"] * (n - 2) + ["y"] * 2
    double_number_combs = list(combinations_with_replacement(range(0, 10), 2))
    # define all permutations of template_number
    for permutation in set(permutations(template_number)):
        permutation = "".join(permutation)
        # provide numbers into template_number
        for d in range(0, 10):
            # define all possible numbers
            template_number = permutation.replace("x", str(d))
            # insert all combination of double numbers to template_number
            for comb in double_number_combs:
                temp_str = template_number.replace("y", str(comb[0]), 1).replace(
                    "y", str(comb[1]), 1
                )
                if temp_str[0] != "0":
                    all_possible_numbers.append(int(temp_str))
                if comb[0] != comb[1]:
                    temp_str = template_number.replace("y", str(comb[1]), 1).replace(
                        "y", str(comb[0]), 1
                    )
                    if temp_str[0] != "0":
                        all_possible_numbers.append(int(temp_str))
    return set(all_possible_numbers)


# function to check which numbers are primes
def check_primes(primes, all_possible_numbers):
    # divide all possible numbers by primes
    for i in range(2, len(primes)):
        if primes[i]:
            all_possible_numbers = [
                number for number in all_possible_numbers if number % i != 0
            ]
    return set(all_possible_numbers)


# function to define: d	    M(10, d)    S(10, d)
def define_results(possible_primes):
    digits_quantity_sum_dict = defaultdict(lambda: [0, 0])
    for number in possible_primes:
        number_str = str(number)
        digit, occurency = Counter(number_str).most_common(1)[0]
        if occurency > digits_quantity_sum_dict[digit][0]:
            digits_quantity_sum_dict[digit] = [occurency, number]
        elif occurency == digits_quantity_sum_dict[digit][0]:
            digits_quantity_sum_dict[digit][1] += number
    return digits_quantity_sum_dict


# main solution function
def solution():
    # get primes numbers below sqrt(N)
    primes = sieve_of_eratosthenes(int(N**0.5))
    # define all possible numbers
    all_possible_numbers = define_numbers()
    # check which numbers are primes
    possible_primes = check_primes(primes, all_possible_numbers)
    digits_quantity_sum_dict = define_results(possible_primes)
    result = 0
    for digit, quantity_sum in digits_quantity_sum_dict.items():
        print(f'Digit: {digit}, quantity: {quantity_sum[0]}, sum: {quantity_sum[1]}')
        result += quantity_sum[1]
    print("Result: {}".format(result))


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("--- %s seconds ---" % (time.time() - start_time))

"""
--- 7.870972633361816 seconds ---
"""
