# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:05:02 2021

Problem 60: Prime pair sets
https://projecteuler.net/problem=60

@author: kuba
"""

import sys

def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

def is_prime_pair_set(a,b):
    if is_prime(int(str(a)+str(b))):
        if is_prime(int(str(b)+str(a))):
            return True
    return False

def solution():  
    prime_list = []
    
    for i in range(3,10**4,2):
        if is_prime(i):
            prime_list.append(i)
    rek(prime_list, [])        
    
def rek(av_primes, prev_primes): 
    for i, current_prime in enumerate(av_primes):
        temp_av_primes = av_primes[i:]
        new_av_primes = [x for x in temp_av_primes if is_prime_pair_set(current_prime,x)]
        new_prev_primes = prev_primes.copy()
        new_prev_primes.append(current_prime)
        if len(new_prev_primes) == 5:
            print(new_prev_primes, sum(new_prev_primes))
            sys.exit()
        else:
            if len(new_av_primes)>0:
                rek(new_av_primes,new_prev_primes)
    
solution()


    


