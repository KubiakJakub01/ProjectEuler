# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:38:39 2022

Problem 108: Diophantine reciprocals I
https://projecteuler.net/problem=108

@author: kuba
"""

'''
SOLUTION IDEA:
    BRUTE FORCE :(
'''

max_n = 524160+1
  
hh = [1] * (max_n + 1);
p = 2;
while((p * p) < max_n):
    if (hh[p] == 1):
        for i in range((p * 2), max_n, p):
            hh[i] = 0;
    p += 1
    
def divCount(n):

    total = 1;
    for p in range(2, n + 1):
        if hh[p] == 1:
            count = 0;
            if (n % p == 0):
                while (n % p == 0):
                    n = int(n / p);
                    count += 1;
                total *= (count + 1);
                  
    return total;

def numberOfSolution(n):
    sum_of_distinct_solutions = 0
    for x in range(n+1, int((n+1)*n/2)):
            y=(n*x)/(x-n)
            if y.is_integer():
                #print('x: {} y: {}'.format(x, y))
                sum_of_distinct_solutions += 1
            if x==y:
                break
    return sum_of_distinct_solutions

def solution():
    sum_of_distinct_solutions = 0
    max_div = 0
    k = 1
    
    #while sum_of_distinct_solutions <= 100:
    #while n <= 10:
    for n in range(int(max_n/3), max_n, 4):
        '''if sum_of_distinct_solutions >= k*100:
            n = n*3
            k += 1'''
        sum_of_distinct_solutions = 0
        #n += 1
        #print('n: {}'.format(n))
        div = divCount(n)
        if div >= max_div:
            max_div = div
            sum_of_distinct_solutions = numberOfSolution(n)
        
        if(sum_of_distinct_solutions>=1000):       
            print('n: {} suma: {} div count: {}\n'.format(n, sum_of_distinct_solutions, divCount(n)))
        
    print('Wynik: {} sum_of_distinct_solutions: {}'.format(n, sum_of_distinct_solutions))

solution()




