# -*- coding: utf-8 -*-
"""
Created on 15.10.2022 18:30

Problem 119: Digit power sum
https://projecteuler.net/problem=119

@author: Jakub

Algoritm description:
    1. Loop through numbers from 2 to 100
    2. Loop through powers from 2 to 15
    3. Calculate number to power
    4. Check if sum of digits is equal to number
    5. If yes, add number to list
    6. Sort list and return 30th element
    7. END
"""

# import libraries
import time

# main solution function
def solution():
    power_number = 1
    number_list = []
    # for every number in (2, 50) generate power if (2, 10)
    for i in range(2, 100):
        for j in range(2, 15):
            power_number = i**j
            if sum([int(x) for x in str(power_number)]) == i:
                number_list.append(power_number)
    return sorted(number_list)[29]


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"Solution found in {time.time() - start_time} seconds")

"""
Solution found in 0.0024766921997070312 seconds
"""
