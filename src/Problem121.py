"""
Created on 14-08-2023

Problem 121: Disc Game Prize Fund
https://projecteuler.net/problem=121

author: KubiakJakub01
"""
import time
from itertools import combinations

import numpy as np

LIMIT = 4

# main solution function
def solution():
    products = []
    # create list of probabilities for each turn
    probabilities = [1 / (i + 1) for i in range(1, LIMIT + 1)]
    # create list of reverse probabilities for each turn
    reverse_probabilities = [1 - i for i in probabilities]
    # create list of all possible combinations
    print(probabilities)
    print(reverse_probabilities)
    for i in range(LIMIT // 2 + 1, LIMIT + 1):
        for comb in combinations(range(LIMIT), i):
            prob = 1
            # create list of all possible products
            for j in range(LIMIT):
                if j in comb:
                    prob *= probabilities[j]
                else:
                    prob *= reverse_probabilities[j]
            products.append(prob)
    print(products)
    # return sum of all products
    return sum(products)


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print("--- %s seconds ---" % (time.time() - start_time))
