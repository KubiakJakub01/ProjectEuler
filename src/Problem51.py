# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:44:15 2021

Problem 51: Prime digit replacements
https://projecteuler.net/problem=51

@author: kuba
"""

import itertools
import numpy as np
import time


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution():
    prime_list = []
    SEARCHING_LEN = 8
    space = np.arange(0, 6)
    combination_list = []

    for r in space[1:-1]:
        temp_comb = [x for x in itertools.combinations(space, r + 1)]
        combination_list += temp_comb

    for i in range(10**5 + 1, 10**6, 2):
        if is_prime(i):
            prime_list.append(str(i))

    const_num = []
    for comb in combination_list:
        temp_list = {}
        # print('comb: {}'.format(comb))
        for i, num in enumerate(prime_list):
            # print(num)
            temp_val = [num[j] for j in comb]
            temp_val = "".join(temp_val)
            temp_list[i] = temp_val

        const_num.append(temp_list)

    for i, nums in enumerate(const_num):
        previous_num = []
        current_comb = list(set(space) - set(combination_list[i]))
        for val in nums.values():
            count = 0
            family_number = []
            if previous_num.count(val) == 0:
                previous_num.append(val)
                current_prime = [prime_list[key] for key, x in nums.items() if x == val]
                # print(current_prime)
                if len(current_prime) >= SEARCHING_LEN:
                    # print('Prime list: {}'.format(current_prime))
                    for prime in current_prime:
                        temp_prime = [prime[x] for x in current_comb]
                        if len(set(temp_prime)) == 1:
                            count += 1
                            family_number.append(prime)
                    # print(count)
                    if count == SEARCHING_LEN:
                        print("comb: {}".format(current_comb))
                        print(family_number)
                        return 0


start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
