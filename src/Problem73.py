# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:08:07 2021

Problem 73: Counting fractions in a range
https://projecteuler.net/problem=73

@author: Admin
"""

def NWD(x, y):
   while(y):
       x, y = y, x % y
   return x

def solution():
    wynik = 0
    
    for d in range(9,12001):
        for n in range(int(d/3), int(d/2)):
            if NWD(d, n) == 1:
                wynik += 1
    print(wynik+3)
solution()
