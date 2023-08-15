"""
Created on 14-08-2023

Problem 121: Disc Game Prize Fund
https://projecteuler.net/problem=121

author: KubiakJakub01
"""
import math
import time
from itertools import combinations

LIMIT = 15

# main solution function
def solution():
    products_sum = 0
    # create list of probabilities for each turn
    probabilities = [1 / (i + 1) for i in range(1, LIMIT + 1)]
    # create list of reverse probabilities for each turn
    reverse_probabilities = [1 - i for i in probabilities]
    # iterate over all winning combinations
    for i in range(LIMIT // 2 + 1, LIMIT + 1):
        for comb in combinations(range(LIMIT), i):
            prob = 1
            # calculate probability of winning
            for j in range(LIMIT):
                if j in comb:
                    prob *= probabilities[j]
                else:
                    prob *= reverse_probabilities[j]
            products_sum += prob
    # return the result
    return math.floor((1 - products_sum) / products_sum) + 1


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print("--- %s seconds ---" % (time.time() - start_time))

"""
--- 0.07505106925964355 seconds ---
"""
