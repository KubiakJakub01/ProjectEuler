# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:23:20 2021

Problem 87: Prime power triples
https://projecteuler.net/problem=87

@author: Admin
"""

import numpy as np

def is_prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def solution():
    N = 50000000
    #N=50
    prime_list = [2]
    memory_dict={}
    
    #Generate prime nums
    for i in range(3,int(N**(1/2))+1,2):
        if is_prime(i):
            prime_list.append(i)
    
    
    #Try brute force solution
    prime_4 = [x for x in prime_list if x<=int(N**(1/4))+1]
    prime_3 = [x for x in prime_list if x<=int(N**(1/3))+1]
    
    #Loop for ^4 power
    for i in prime_4:
        n_4 = i**4
        #Loop for ^3 power
        for j in prime_3:
            n_3 = j**3
            if n_3+n_4>N:
                break
            #Loop for ^2 power
            for k in prime_list:
                n_2 = k**2
                temp_sum = n_2+n_3+n_4
                if N > temp_sum:                        
                    memory_dict[temp_sum] = 1
                else:
                    break
                
    print(sum(memory_dict.values()))
    
solution()