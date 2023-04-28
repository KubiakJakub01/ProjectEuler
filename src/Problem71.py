# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:47:21 2021

Problem 71: Ordered fractions
https://projecteuler.net/problem=71

@author: kuba
"""


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution():
    value = 3 / 7
    denominator = 1000000
    min_diff = 1
    min_fraction = []
    start_n = 1

    for d in range(2, denominator + 1):
        for n in range(start_n, d):
            fraction = n / d
            if fraction < value:
                if nwd(n, d) == 1:
                    diff = value - fraction
                    if diff < min_diff:
                        min_diff = diff
                        min_fraction = [n, d]
            else:
                start_n = n - 1
                break
    print(min_fraction)


solution()
