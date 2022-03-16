# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:30:47 2020


Problem 25: 1000-digit Fibonacci number

    The Fibonacci sequence is defined by the recurrence relation:
    
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

@author: Admin
"""


'''def fib(n):
    if n == 0 or n == 1: return 1
    else: return fib(n-2)+fib(n-1)'''
    

def solution():
    fibo_tab = [1,1]
    
    for i in range(0,10000):
        n = fibo_tab[-1]+fibo_tab[-2]
        fibo_tab.append(n)
        
        if len(str(n))==1000:
            print('fib_{} {} len: {}'.format(len(fibo_tab),n,1000))
            break
        
solution()

