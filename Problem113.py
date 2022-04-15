# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:01:36 2022

Problem 113: Non-bouncy numbers
https://projecteuler.net/problem=113

@author: kuba
"""

'''
Output:
    51161058134250
--- 0.0 seconds ---

Stopień trudnosci: 30%
'''

import time

def silnia(n):
    wynik = 1
    for i in range(2,n+1):
        wynik *= i
    return wynik

def newton(n,k):
    return silnia(n)/(silnia(k)*silnia(n-k))

def solution():
    k = 100
    wynik = 0
    wynik = int((newton(k + 10, 10) + newton(k + 9, 9) - 2 - 10 * k))
    print(wynik)
        
 
   
start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))