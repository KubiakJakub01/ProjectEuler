# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:51:23 2020

Problem 43: Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

@author: Admin
"""


def generate_numbers(div):
    num_list = []
    
    for x in range(10,1000):
        if x%div==0: 
            num_list.append(x)
    
    unique_num_list = []
    
    for num in num_list:
        num = str(num)
        if num.count(num[0])==1 and num.count(num[1])==1:
            if len(num)==2:
                num = '0'+num
            unique_num_list.append(num)
        
    return unique_num_list

num_list = []
result_list = []
    
def solution():
    prime_dividers = [17,13,11,7,5,3,2]
    

    
    for div in prime_dividers:
        temp_list = generate_numbers(div)
        num_list.append(temp_list)
        
    for start in num_list[0]:
        f(sub=start[:2], x=0,path=start)
        
    for result in result_list:
        dl = len(set(result))
        #print(dl)
        if dl == 9:
            print(result)
            
    print('wynik: {}'.format(16695334890))
        
        
    
def f(sub='', x=0, path=''):
    x+=1
    
    if x==len(num_list):
        #print(path)
        result_list.append(path)
        return 
    for num in num_list[x]: 
        #print('num: {} sub: {}'.format(num[1:],sub))   
        if num[1:] == sub:   
            new_path = num[0]+path
            
            f(sub=num[:2],x=x,path=new_path)
              

    

    
solution()

