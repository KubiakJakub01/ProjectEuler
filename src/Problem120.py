# -*- coding: utf-8 -*-
"""
Created on 15.10.2022 20:30

Problem 120: Square remainders
https://projecteuler.net/problem=120

@author: Jakub

Algoritm description:
    1. Loop through numbers from 3 to 1000
    2. If number is even, add (a-2)*a to result
    3. If number is odd, add (a-1)*a to result
    4. END
"""

# import libraries
import time


# main solution function
def solution():
    result = 0
    for a in range(3, 1001):
        if a % 2 == 0:
            result += (a - 2) * a
        else:
            result += (a - 1) * a
    return result


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"Solution found in {time.time() - start_time} seconds")

"""
Solution found in 0.0001780986785888672 seconds
"""
