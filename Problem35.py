# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:47:13 2021

Problem 35: Circular primes
https://projecteuler.net/problem=35

@author: kuba
"""

import itertools
import time

def is_prime(n):   
    liczba = int(''.join([str(s) for s in n]))
    for i in range(2, int(liczba**(1/2))+1):
        if liczba%i == 0:
            return False
    return True

def check_circular(n):
    n = list(n)
    for i in range(len(n)):
        if not is_prime(n):
            return False
        element = n.pop(0)
        n.append(element)
    return True



def solution():
    number_list = [1,3,7,9]
    nums = []
    history = []
    wynik = 1
    
    for i in range(1,7):
        for x in itertools.combinations_with_replacement(number_list, i):
            nums.append(list(set(itertools.permutations(x))))
            
    for num in nums:
        if len(num) == 1 and is_prime(num[0]):
            #history.append(int(''.join([str(s) for s in num[0]])))
            wynik += 1     
        else:
            for n in num:
                if check_circular(n):
                    #history.append(int(''.join([str(s) for s in n])))
                    wynik += 1
                    
    #print('wynik: {} history: {}'.format(wynik, history))
    print(wynik)
  
start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
