# -*- coding: utf-8 -*-
"""
Problem 56(Powerful digit sum)
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def solution():
    max_num = 0
    max_i = 0
    max_j = 0
    
    for i in range(11, 101):
        for j in range(11,101):  
            suma = sum(map(int, str(pow(i,j))))
            if max_num < suma:
                max_num = suma
                max_i = i
                max_j = j              
    print("Wynik: {} dla {}^{}".format(max_num, max_i, max_j))
                
solution()

