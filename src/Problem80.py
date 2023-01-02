# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:20:15 2021

Problem 80: Square root digital expansion
https://projecteuler.net/problem=80

@author: Admin
"""


from decimal import *


def solution():
    
    #Init base variablies 
    result = 0    
    getcontext().prec = 102 '''We need to larger precision to avoid rounding'''
    suma = 0
    irrational_num = [x for x in range(2,101) if not (x**(1/2)).is_integer()] '''Generate numbers < 100 which square have irrational expansion'''

    #Main loop
    for root in irrational_num:
        x = str(Decimal(root).sqrt()).replace('.','')[:100]
        suma = sum([int(i) for i in x])
        result+=suma

    print(result)
    
solution()


