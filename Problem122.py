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

NUMBER_RANGE = set(range(1,201))

# main solution function
def solution() -> int:
    # init variables
    result = 1
    level_dict = defaultdict(set)
    level_dict[0] = set([1])
    level_dict[1] = set([2])
    current_level_key = 1
    nubmers_list = [1, 2]
    previosu_layers_number_list = [1]
    # main loop
    while len(nubmers_list) < 200:
        current_level_key += 1
        current_level_number_list = level_dict[current_level_key-1]
        # define new level by making all possible combinations of previous layers with current level
        next_level_number_list = set([x+y for x in current_level_number_list for y in previosu_layers_number_list+[x] if x+y not in nubmers_list and x+y <= 200]) 
        # result is sum of level*len(level)
        result += current_level_key*len(next_level_number_list)
        # add new level to dictionary
        level_dict[current_level_key] = next_level_number_list
        # update previous layers list and numbers list
        previosu_layers_number_list += current_level_number_list
        nubmers_list += next_level_number_list
        # print(f"Level {len(level_dict)}: {next_level_number_list} number_list: {nubmers_list} previous_layers: {previosu_layers_number_list}")
    # print(level_dict)
    double_check_result = 0
    print(sorted(nubmers_list), len(nubmers_list))
    for key, value in level_dict.items():
        print(f"Level {key}: {value}")
        double_check_result += key*len(value)
    print(f"Double check result: {double_check_result}")
    return result

if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"Solution found in {time.time() - start_time} seconds")
