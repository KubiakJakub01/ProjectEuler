# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:32:25 2021

Problem 89: Roman numerals
https://projecteuler.net/problem=89

@author: Admin
"""

roman_nums = []

with open('roman.txt') as num:
    roman_nums = num.readlines()

roman_nums = [x.strip() for x in roman_nums]

roman_dictonary = {'M':1000,
    'CM': 900,
    'D':500,
    'CD':400,
    'C':100,
    'XC':90,
    'L':50,
    'XL':40,
    'X':10,
    'IX':9,
    'V':5,
    'IV':4,
    'I':1}

def roman_2_num(roman_num):
    int_num = 0
    
    for i in range(0,len(roman_num)):
        if i>0 and roman_dictonary[roman_num[i]] > roman_dictonary[roman_num[i-1]]:
            int_num += roman_dictonary[roman_num[i]]-2*roman_dictonary[roman_num[i-1]]
        else:
            int_num+=roman_dictonary[roman_num[i]]

    return int_num



def num_2_roman(num):
    roman_num = ''
    i = 0
    for symbol, val in roman_dictonary.items():
        for _ in range(num // val):
            roman_num += symbol
            num -= val
        i += 1
    return roman_num
    

def solution():
    result = 0
    
    for roman in roman_nums:
        correct_roman_num = num_2_roman(roman_2_num(roman))
        if roman == correct_roman_num:
            result += 1
        else:
            print('roman: {} correct: {}'.format(roman,correct_roman_num))
    print(result)


solution()


def solution_1():
    
    
    result = 0
    valid_dict = {'I': ['V','X'], 'X': ['C', 'L'], 'C': ['D','M']}
    
    for num in roman_nums:
        prev_n = num[0]
        is_correct = True
        count = 1
        for n in num[1:]:
            if roman_dictonary[n] > roman_dictonary[prev_n]:
                if n not in valid_dict[prev_n]:
                    is_correct = False
                    break
            if prev_n == n:
                count += 1
            else:
                if count == 4 and prev_n != 'M':
                    is_correct = False
                    break
                count = 1
            prev_n = n
        if is_correct:
            result += 1
        else:
            print(num)
    print(result)
