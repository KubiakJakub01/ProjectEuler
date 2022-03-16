# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:03:27 2021

Problem 100: Arranged probability
https://projecteuler.net/problem=100

@author: Admin
"""

import math

def solution():
    
    blue = 85
    red = 35
    
    n = 20
    limit = 10**5
    coff = 5.7
    
    #for n in range(20,10000):
    while n < limit:
        i = math.floor(n*0.7)
        result = 0
        while result < 0.5:
            result = (i*(i-1))/(n*(n-1))

            
            if result == 0.5:
                #print('{}/{} * {}/{} == 0.5'.format(i,n,i-1,n-1))
                
                print('{}*{}/{}*{}'.format(i,i-1,n,n-1))
                n = int(n*coff)
            
            i+=1
        
        n+=1
    
#solution()

k = 2
nr = 7
stala = (k+1)*nr
rozmiar = 10+k
inc = 12
start = 100+nr
tab1 = [start]
tab2 = []
suma1 = 0
suma2 = 0 

for i in range(1,rozmiar):   
    tab1.append((tab1[-1]+inc)) 
    
[tab2.append(x+stala) for x in tab1]

suma1 = sum(tab1)
suma2 = sum(tab2)

print("tab1: {} i suma: {}".format(tab1, suma1))
print("tab2: {} i suma: {}".format(tab2, suma2))
print("roznica: {} iloczyn: {}".format(suma2-suma1, rozmiar*stala))


    
