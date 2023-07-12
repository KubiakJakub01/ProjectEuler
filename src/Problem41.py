# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:51:39 2021

Problem 41: Pandigital prime

@author: kuba
"""

import numpy as np
import itertools


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def conv_to_num(l):
    l = [str(s) for s in l]
    return int("".join(l))


def solution():
    nums = np.arange(1, 8)

    permutations = [conv_to_num(x) for x in set(itertools.permutations(nums))]

    for n in sorted(permutations, reverse=True):
        if is_prime(n):
            print(n)
            return


solution()
