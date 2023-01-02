# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:16:35 2021

Problem 32: Pandigital products
https://projecteuler.net/problem=32
 
@author: kuba
"""

import itertools
import numpy as np
import collections

def conv_to_num(n):
    n = [str(s) for s in n]
    n = "".join(n) 
    n = int(n) 

    return n    
  
def solution():  
    list_of_number = np.arange(1,10)
    suma = 0
    historia = []
    his = []
    net_list = [[1,4], [2,3], [2,2]]    

    for net in net_list:
        for x in itertools.combinations(list_of_number, net[0]):
            temp_list = np.setdiff1d(list_of_number,x)
            for y in itertools.combinations(temp_list, net[1]):
                result_num = np.setdiff1d(temp_list,y)   
                result_num = list(result_num)
                for n in itertools.permutations(y):
                    n = conv_to_num(n)
                    for m in itertools.permutations(x):
                        m = conv_to_num(m)
                        res = m*n
                        res_list = [int(a) for a in str(res)]
                        if len(res_list) == len(result_num):
                            if collections.Counter(res_list) == collections.Counter(result_num) and (his.count(res)==0):
                                #print('l1: {} l2: {}'.format(res_list, result_num))
                                historia.append([m,n,res])
                                his.append(res)
                                suma += res
                        
    print('Historia: {} wynik: {}'.format(historia, suma))
    
solution()
