# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:26:09 2021

Problem 68: Magic 5-gon ring
https://projecteuler.net/problem=68

@author: kuba
"""

'''
6357528249411013
'''

from itertools import permutations  

def filling_magic_ring(suma, i, rest_nums, core):
    if len(rest_nums) == 0:
        result = ''
        
        for note in core:
            for s in note:
                result += str(s)
                
        print(result)
        return
    
    else:
        n = suma - sum(core[i])
        if rest_nums.count(n):
            core[i].insert(0, n)
            i+=1
            rest_nums.remove(n) 
            filling_magic_ring(suma,i,rest_nums,core)
            
        else:
            return



def solution():
    lim = 6
    
    core_nums = list(range(1,lim))
    rest_nums = list(range(lim,11))
    
    for perm in permutations(core_nums):
        perm = list(perm)
        perm.append(perm[0])
        
        perm = [[perm[i], perm[i+1]] for i in range(0,5)]
       
        for n in rest_nums:
            j=0
            temp_rest_nums = rest_nums.copy()
            suma = n+sum(perm[j])
            
            core = [x.copy() for x in perm]            
            core[j].insert(0, n)
            j+=1
            temp_rest_nums.remove(n)
            filling_magic_ring(suma, j, temp_rest_nums.copy(), core)
            
solution()
    