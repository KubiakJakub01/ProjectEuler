# -*- coding: utf-8 -*-
"""
Created on 21-09-2022 21:47

Problem 90: Cube digit pairs
https://projecteuler.net/problem=90

@author: Jakub

Algoritm description:
    1. Create a list of all possible combinations of 6 dice:
        with 6 and 9 as one number
    2. Create a list of all possible combinations of two dice
        which meet the condition of separate pairs
    3. Check if the combination of two dice is valid
    4. END
"""

# import libraries
import time
from itertools import combinations

ALLOWED_NUMBERS = set(range(10))
REQUESTED_NUMBERS = set([0, 1, 2, 3, 4, 5, 6, 8])
SEPARATE_PAIRS = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)]


# function to create a list of all possible combinations of 6 number in dice
def create_dice_list():
    for dice in list(combinations(ALLOWED_NUMBERS, 6)):
        if 6 in dice and 9 not in dice:
            yield dice + (9,)
        elif 9 in dice and 6 not in dice:
            yield dice + (6,)
        else:
            yield dice


# function to check if the combination of two dice is valid
def is_valid_dice_pair(dice_pair):
    for pair in SEPARATE_PAIRS:
        if pair[0] in dice_pair[0] and pair[1] in dice_pair[1]:
            continue
        if pair[0] in dice_pair[1] and pair[1] in dice_pair[0]:
            continue
        return False
    if REQUESTED_NUMBERS.issubset(set(dice_pair[0] + dice_pair[1])):
        return True
    return False


# function to create a list of all possible combinations of two dice
def create_dice_pairs_list(dice_list):
    count_dice_pairs = 0
    for dice_pair in list(combinations(dice_list, 2)):
        if is_valid_dice_pair(dice_pair):
            count_dice_pairs += 1
    return count_dice_pairs


# main solution function
def solution():
    dice_list = create_dice_list()
    count_dice_pairs = create_dice_pairs_list(dice_list)
    print(count_dice_pairs)


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("--- %s seconds ---" % (time.time() - start_time))

"""
--- 0.032662153244018555 seconds ---
"""
