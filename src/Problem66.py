# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:52:40 2021

Problem 66: Diophantine equation
https://projecteuler.net/problem=66

@author: Admin
"""

import math

def solvePell(n):
    x = int(math.sqrt(n))
    y, z, r = x, 1, x << 1
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (n - y * y) // z
        r = (x + y) // z
 
        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r
 
        a, b = f2 * x + e2, f2
        if a * a - n * b * b == 1:
            return a, b

def solution():
    D = [x for x in range(2,1001) if not (x**(1/2)).is_integer()]
    max_x = 0
    max_d = 0
    for d in D:
        x,y = solvePell(d)
        if x > max_x:
            max_x = x
            max_d = d
        
    print('x: {} d: {}'.format(max_x, max_d))
        
        
solution()
            