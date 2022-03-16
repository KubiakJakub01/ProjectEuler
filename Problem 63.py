# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:56:11 2020

Problem 63: Powerful digit counts

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

@author: Admin
"""

def solution():
    tab = []
    for i in range(1,22):
        for j in range(1,10):
            potega = pow(j,i)
            if len(str(potega)) == i: tab.append(potega)
                
    #print(tab)
    print('wynik: {}'.format(len(tab)))
    
solution()