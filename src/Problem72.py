# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:04:37 2021

Problem 72: Counting fractions
https://projecteuler.net/problem=72

@author: Admin
"""

import numpy as np

def solution():
    limit = 1000000
    phi = np.arange(0,limit+1)
    result = 0
    
    for i in range(2,limit+1):
        if phi[i] == i:
            for j in range(i,limit+1, i):
                phi[j] = phi[j] / i * (i-1)
        result += phi[i]
        
    print(result)

        
solution()

