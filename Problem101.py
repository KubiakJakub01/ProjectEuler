# -*- coding: utf-8 -*-
"""
Created on 24-09-2022 17:09

Problem 101: Optimum polynomial
https://projecteuler.net/problem=101

@author: Jakub

Algoritm description:
    1. Loop x through degree of polynomial
    2. Determine point of polynomial for current x
    3. Create level_dict where under key 0 is list of points of polynomial
        and under next keys are list of differences between two last elements from previous level
        till x+1 where is the last element
    4. Sum last elements from all lists in level_dict which is BOP for current x   
    5. Sum all BOPs and return the result
    6. END
"""

# import libraries
import time
from collections import defaultdict

# given coefficients:
# 1 − n + n2 − n3 + n4 − n5 + n6 − n7 + n8 − n9 + n10
COEFFICIENTS = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
N = len(COEFFICIENTS) - 1

# polunomial function
def polynomial(x, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result += coefficients[i] * x**i
    return result


# main solution function
def solution():
    level_dict = defaultdict(list)
    level_dict[0] = [1]
    BOP = [1]
    for x in range(2, N + 1):
        level_dict[0].append(polynomial(x, COEFFICIENTS))
        for key in level_dict.keys():
            if key == 0:
                current_val = level_dict[key][-1] - level_dict[key][-2]
            else:
                level_dict[key].append(current_val)
                current_val = level_dict[key][-1] - level_dict[key][-2]
        level_dict[len(level_dict.keys()) + 1].append(current_val)
        bop = sum([value[-1] for value in level_dict.values()])
        BOP.append(bop)
    return BOP


if __name__ == "__main__":
    start_time = time.time()
    BOP = solution()
    print(f"BOP: {BOP} sum: {sum(BOP)}")
    print("--- %s seconds ---" % (time.time() - start_time))

"""
--- 0.0009975433349609375 seconds ---
"""
