# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:08:30 2022

Problem 106: Special subset sums: meta-testing
https://projecteuler.net/problem=106

@author: kuba
"""

from itertools import combinations


def solution():
    n = 4
    comb = []
    for i in range(1, n):
        comb += list(combinations(range(n), i))
    print(comb)
    print(len(comb))


solution()
