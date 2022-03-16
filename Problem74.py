# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:02:23 2020

Problem 74: Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

@author: Admin
"""

factorials = [1]
    
for i in range(1,10):
    j = factorials[i-1]*i
    factorials.append(j)
    


def new_factor(num):
    new_f = 0
    temp_num = str(num)
    for x in temp_num:
        new_f += factorials[int(x)]
        
    return new_f


def solution():
    
    len_tab = []
    for number in range(1,1000000):
        num_list = [number]
        new_num = new_factor(number)
        
        while new_num not in num_list:
            num_list.append(new_num)
            new_num = new_factor(new_num)
            
        len_tab.append(len(num_list))
    print(len_tab.count(60))
            
 
solution()