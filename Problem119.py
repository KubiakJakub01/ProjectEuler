# -*- coding: utf-8 -*-
"""
Created on 15.10.2022 18:30

Problem 119: Digit power sum
https://projecteuler.net/problem=119

@author: Jakub

Algoritm description [Draft]:
"""

# import libraries
import time
import math

# main solution function
def solution():
    n = 1
    number_list = []
    # for every number in (2, 50) generate power if (2, 10)
    for i in range(2, 100):
        for j in range(2, 15):
            n = i**j
            if sum([int(x) for x in str(n)]) == i:
                number_list.append(n)
    return sorted(number_list)[29]
                
                

if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"Solution found in {time.time() - start_time} seconds")

"""
Solution found in 0.0024766921997070312 seconds
"""
