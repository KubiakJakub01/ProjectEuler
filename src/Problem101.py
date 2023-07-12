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
TEST_COEFFICIENTS = [0, 0, 0, 1]
N = len(TEST_COEFFICIENTS)

# polunomial function
def polynomial(x, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result += coefficients[i] * x**i
    return result


# main solution function
def solution():
    b = []
    BOP = []
    for x in range(1, N + 1):
        coefficients_metrix = []
        for n in range(1, x + 1):
            coefficients_metrix.append([n**m for m in range(0, x)])
        a = np.array(coefficients_metrix)
        b.append(polynomial(x, TEST_COEFFICIENTS))
        X = np.linalg.solve(a, b)
        print(X)
        BOP.append(int(polynomial(x + 1, X)))
    return BOP


if __name__ == "__main__":
    start_time = time.time()
    BOP = solution()
    print(f"BOP: {BOP} sum: {sum(BOP)}")
    print("--- %s seconds ---" % (time.time() - start_time))

"""
--- 0.0009975433349609375 seconds ---
"""
