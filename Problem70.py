# -*- coding: utf-8 -*-
"""
Problem 70 (Totient permutation)
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, 
for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

import math

def solution():
    min_ = math.inf
    n = 0
    #for i in range(pow(10,5), pow(10,6)):
    for i in range(pow(10,6),pow(10,7)):
        produce = int(phi(i))
        #print('produce: {}'.format(produce))
        if sorted(str(i)) == sorted(str(produce)):   
            print('Trueee')
            if min_ > i/produce:
                min_ = i/produce
                n = i
    print("Wynik: {} dla: {}".format(min_, n))
    
    
def phi(n=1):
    if is_prime(n):
        return n-1
    
    result = n
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            while n%i==0:
                n /= i
            result -= result/i
    if n > 1:
        result -= result / n
    return result
    
def is_prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number%i==0:
            return False
    return True

solution()