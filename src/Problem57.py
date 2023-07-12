# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:30:52 2021

Problem 57: Square root convergents
https://projecteuler.net/problem=57

@author: kuba
"""

import time


def solution():
    # Main score
    score = 0
    # [[x,y]] where x - numerator, y - denominator
    list_of_number = [[3, 2], [7, 5]]

    # Main loop
    for i in range(1, 1000):
        # Using formula for next expresion
        numerator = list_of_number[i][0] * 2 + list_of_number[i - 1][0]
        denominator = list_of_number[i][1] * 2 + list_of_number[i - 1][1]
        if len(str(numerator)) > len(str(denominator)):
            score += 1
        list_of_number.append([numerator, denominator])

    print(score)


start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
