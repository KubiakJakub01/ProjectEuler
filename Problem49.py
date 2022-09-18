# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:14:50 2021

Problem 49: Prime permutations
https://projecteuler.net/problem=49

@author: kuba
"""

import numpy as np
import itertools
import time

def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return 0
    return n

def solution():
    numbers = np.arange(1,10)
   
    for combi in itertools.combinations_with_replacement(numbers, 4):
        prime_permutation_list = []
        for perm in set(itertools.permutations(combi)):
            n = [str(s) for s in perm]
            n = int(''.join(n))
            if is_prime(n):
                prime_permutation_list.append(n)
        l = len(prime_permutation_list)
        #print(prime_permutation_list)
        if l > 2:
            prime_permutation_list.sort()
            #print(prime_permutation_list)
            for i in range(0,l-1):
                current_number = prime_permutation_list[i]
                for j in range(i+1,l):
                    diff = prime_permutation_list[j] - current_number
                    if prime_permutation_list.count(current_number+2*diff):
                        print('{} {} {}'.format(current_number, current_number+diff, current_number+diff*2))
                        #return 0

            
start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))