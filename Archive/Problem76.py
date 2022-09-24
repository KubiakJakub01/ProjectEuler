# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:45:12 2019

@author: Colinx

Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

result = 0

def wouuld(number, bigest_prev_num=1, s=''):
    global result
    new_num = int(number/2)+1
    new_s = ''
    if bigest_prev_num <= new_num:
        for i in range(bigest_prev_num, new_num):
            new_s = s+str(i)
            result += 1
           
            #print("Liczba: {} big_prev: {}".format(new_num-1, i))
            wouuld(number=number-i, bigest_prev_num=i, s=new_s)
        #print("Ciag: {}".format(new_s))

def solution():
    global result
    #for i in range(3, 10):
    wouuld(1000)
    print("Wynik: {} dla {}".format(result, 1000))
    result = 0
    return 


solution()