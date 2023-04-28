# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:20:55 2021

Problem 75: Singular integer right triangles
https://projecteuler.net/problem=75

@author: Admin
"""


import numpy as np
from math import gcd


def solution():
    L = 1500000
    pt = set()
    for m in range(1, int((L / 2) ** 0.5)):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m, n) == 1:
                pt.add(2 * m * (m + n))

    table = np.zeros(L + 1)
    for j in pt:
        table[j::j] += 1
    print(table.size - np.count_nonzero(table - 1))


solution()
