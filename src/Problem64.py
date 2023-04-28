# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:55:50 2021

Problem 64: Odd period square roots
https://projecteuler.net/problem=64

@author: kuba
"""

import math


def period_length(n):
    period = 0
    end_flag = True
    a_0 = math.floor(n ** (1 / 2))
    b = a_0
    b_0 = a_0
    c = n - a_0**2
    c_0 = c

    factors_list = []
    while end_flag:
        a = math.floor((a_0 + b) / c)
        b = a * c - b
        c = (n - b**2) / c

        # factors_list.append(a)
        period += 1

        """if a == 2*a_0:            
           if len(factors_list) == 1:               
               end_flag = False
               
           elif factors_list[0] == factors_list[-2]:
               end_flag = False"""
        if a == 2 * a_0:
            end_flag = False

    return period


def is_not_square_int(n):
    square = n ** (1 / 2)
    if square.is_integer():
        return False
    return True


def solution():
    N = 10000
    result = 0

    for n in range(2, N + 1):
        if is_not_square_int(n):
            period = period_length(n)
        else:
            continue

        if period % 2 == 1:
            result += 1

    print(result)


solution()
