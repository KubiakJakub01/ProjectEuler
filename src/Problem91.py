# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:38:18 2022

Problem 91: Right triangles with integer coordinates
https://projecteuler.net/problem=91

@author: kuba
"""


import math


def solution():
    size = 50
    result = size * size * 3
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            fact = math.gcd(x, y)
            result += min(int(y * fact / x), int((size - x) * fact / y)) * 2

    print(result)


solution()
