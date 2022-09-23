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
from itertools import permutations, combinations

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
    template_number = ['x'] * (n-2) + ['y'] * 2
    double_number_combs = list(combinations(range(0,10), 2))
    # define all permutations of template_number
    for permutation in set(permutations(template_number)):
        permutation = ''.join(permutation)
        # provide numbers into template_number
        for d in range(0,10):
            # define all possible numbers
            template_number = permutation.replace('x', str(d))
            #all_possible_numbers.append([temp_num.replace('y', str(y)) for y in range(10)])
            # insert all combination of double numbers to temp_num
            for comb in double_number_combs:
                temp_num = template_number
                all_possible_numbers.append(temp_num.replace('y', str(comb[0]), 1).replace('y', str(comb[1]), 1))
                all_possible_numbers.append(temp_num.replace('y', str(comb[1]), 1).replace('y', str(comb[0]), 1))
    return all_possible_numbers


# main solution function
def solution():
    # get primes numbers below sqrt(N)
    #primes = sieve_of_eratosthenes(int(N**0.5))
    # print len of true primes
    #print(sum(primes))
    # define all possible numbers
    all_possible_numbers = define_numbers()
    print(all_possible_numbers[:100])


if __name__ == "__main__":
    #start_time = time.time()
    solution()
    #print("--- %s seconds ---" % (time.time() - start_time))