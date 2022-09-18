# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:25:47 2021

Problem 92: Square digit chains
https://projecteuler.net/problem=92

@author: kuba
"""
import itertools
import numpy as np

def f(x, dict_num):
    if dict_num[x] != -1:
        return dict_num[x]

    new_x = sum([int(i)**2 for i in str(x)])
    dict_num[x] = f(new_x,dict_num)
    return dict_num[x]

def solution():
    N = 10000000
    s_N = 9**2*7+1
    space = np.arange(0,10)
    result = 0
    dict_num = {x: -1 for x in range(0,s_N)}
    dict_num[0] = 0
    dict_num[1] = 0
    dict_num[89] = 1

    for i in range(2,s_N):
        f(i, dict_num)

    '''result = list(dict_num.values()).count(1)
    for j in range(s_N+1, N):
        new_n = sum([int(i)**2 for i in str(j)])
        result += dict_num[new_n]'''
        
    for r in range(1,8):
        for comb in itertools.combinations_with_replacement(space,r):
            n = sum([x**2 for x in comb])
            if n >= s_N:
                print(comb)
            result += dict_num[n]
            
    print(result)

solution()
