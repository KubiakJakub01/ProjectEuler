# -*- coding: utf-8 -*-
"""
Created on 16.10.2022 12:38
Problem 122: 
https://projecteuler.net/problem=122
@author: Jakub
Algoritm description [draft]:
"""

# imports libraries
import time
from collections import defaultdict

# main solution function
def solution():
    # init variables
    level_dict = defaultdict(list)
    level_dict[0] = [1]
    level_dict[1] = [2]
    nubmers_list = [1, 2]
    # main loop
    for i in range(10):
        current_level = len(level_dict) + 1
        # numbers in current level are sum of number in previous level and number in levels before previous
        for number in level_dict[current_level - 1]:
            new_numbers = [x + number for level_number in range(0, current_level - 1) for x in level_dict[level_number]  if x + number not in nubmers_list]
            print(new_numbers)
            level_dict[current_level].extend(new_numbers)
            nubmers_list += new_numbers
        print(current_level, level_dict[current_level])
    # final result is sum of level_number*number_of_numbers_in_level
    result = sum([level_number*len(level_dict[level_number]) for level_number in level_dict])
    #print(level_dict)
    return result

if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"Solution found in {time.time() - start_time} seconds")
