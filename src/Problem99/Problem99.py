# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:17:32 2021

Problem 99: Largest exponential
https://projecteuler.net/problem=99

@author: kuba
"""

PATH_2_FILE = 'base_exp.txt'
bufor_list = []
base_exp_list = []
with open(PATH_2_FILE) as p:
    bufor_list = p.readlines()


def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

def solution():
    max_exp = 0
    id_max_val = 0
    max_val = 0
    
    for base_exp in bufor_list:
        base_exp = base_exp.strip().split(',')
        base_exp = [int(x) for x in base_exp]
        if base_exp[1]>max_exp:
            max_val = base_exp[0]
            max_exp = base_exp[1]           
        
        base_exp_list.append(base_exp)

    print('max exp: {}'.format(max_exp))    
    for i, base_exp in enumerate(base_exp_list):
        current_val = base_exp[0]**(base_exp[1]/max_exp)
        
        if current_val > max_val:
            print('{}^{} val: {}'.format(base_exp[0], base_exp[1], current_val))
            max_val = current_val
            id_max_val = i
            
    print('wynik: {} <> {}'.format(id_max_val, base_exp_list[id_max_val]))
    
solution()
