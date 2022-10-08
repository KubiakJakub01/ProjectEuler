# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:17:36 2021

Problem 93: Arithmetic expressions
https://projecteuler.net/problem=93

@author: kuba
"""

'''
51 [1, 2, 5, 8]
'''

operations = ['+', '-', '*', '/']

def compute(nums, x, result_list):
    if len(nums) == 0:
        x = float(x)
        if x.is_integer() and x>0:
            #print('x: {}'.format(x))
            result_list.append(x)
    else:
        for num in nums:
            new_nums = nums.copy()
            new_nums.remove(num)
            
            #print(new_nums)
            # +
            new_x = x+num
            compute(new_nums, new_x, result_list)
            
            # -
            new_x = x-num
            compute(new_nums, new_x, result_list)
            new_x = num-x
            compute(new_nums, new_x, result_list)
            
            # *
            new_x = x*num
            compute(new_nums, new_x, result_list)
            new_x = (-1)*x*num
            compute(new_nums, new_x, result_list)
            
            # /
            if x != 0 and num != 0:
                new_x = x/num
                compute(new_nums, new_x, result_list)
                #new_x = (-1)*x/num
                #compute(new_nums, new_x, result_list)
                new_x = num/x
                #compute(new_nums, new_x, result_list)
                #new_x = (-1)*num/x
                compute(new_nums, new_x, result_list)

    return 0

def consecutive_int(list_of_nums):   
    result = 0
    for i in range(0, len(list_of_nums)):
        if list_of_nums[i] == i+1:
            result += 1
        else:
            return result
        
    return result

def solution():
    lista = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 8], [1, 2, 3, 9], [1, 2, 4, 5], [1, 2, 4, 6], [1, 2, 4, 7], [1, 2, 4, 8], [1, 2, 4, 9], [1, 2, 5, 6], [1, 2, 5, 7], [1, 2, 5, 8], [1, 2, 5, 9], [1, 2, 6, 7], [1, 2, 6, 8], [1, 2, 6, 9], [1, 2, 7, 8], [1, 2, 7, 9], [1, 2, 8, 9], [1, 3, 4, 5], [1, 3, 4, 6], [1, 3, 4, 7], [1, 3, 4, 8], [1, 3, 4, 9], [1, 3, 5, 6], [1, 3, 5, 7], [1, 3, 5, 8], [1, 3, 5, 9], [1, 3, 6, 7], [1, 3, 6, 8], [1, 3, 6, 9], [1, 3, 7, 8], [1, 3, 7, 9], [1, 3, 8, 9], [1, 4, 5, 6], [1, 4, 5, 7], [1, 4, 5, 8], [1, 4, 5, 9], [1, 4, 6, 7], [1, 4, 6, 8], [1, 4, 6, 9], [1, 4, 7, 8], [1, 4, 7, 9], [1, 4, 8, 9], [1, 5, 6, 7], [1, 5, 6, 8], [1, 5, 6, 9], [1, 5, 7, 8], [1, 5, 7, 9], [1, 5, 8, 9], [1, 6, 7, 8], [1, 6, 7, 9], [1, 6, 8, 9], [1, 7, 8, 9], [2, 3, 4, 5], [2, 3, 4, 6], [2, 3, 4, 7], [2, 3, 4, 8], [2, 3, 4, 9], [2, 3, 5, 6], [2, 3, 5, 7], [2, 3, 5, 8], [2, 3, 5, 9], [2, 3, 6, 7], [2, 3, 6, 8], [2, 3, 6, 9], [2, 3, 7, 8], [2, 3, 7, 9], [2, 3, 8, 9], [2, 4, 5, 6], [2, 4, 5, 7], [2, 4, 5, 8], [2, 4, 5, 9], [2, 4, 6, 7], [2, 4, 6, 8], [2, 4, 6, 9], [2, 4, 7, 8], [2, 4, 7, 9], [2, 4, 8, 9], [2, 5, 6, 7], [2, 5, 6, 8], [2, 5, 6, 9], [2, 5, 7, 8], [2, 5, 7, 9], [2, 5, 8, 9], [2, 6, 7, 8], [2, 6, 7, 9], [2, 6, 8, 9], [2, 7, 8, 9], [3, 4, 5, 6], [3, 4, 5, 7], [3, 4, 5, 8], [3, 4, 5, 9], [3, 4, 6, 7], [3, 4, 6, 8], [3, 4, 6, 9], [3, 4, 7, 8], [3, 4, 7, 9], [3, 4, 8, 9], [3, 5, 6, 7], [3, 5, 6, 8], [3, 5, 6, 9], [3, 5, 7, 8], [3, 5, 7, 9], [3, 5, 8, 9], [3, 6, 7, 8], [3, 6, 7, 9], [3, 6, 8, 9], [3, 7, 8, 9], [4, 5, 6, 7], [4, 5, 6, 8], [4, 5, 6, 9], [4, 5, 7, 8], [4, 5, 7, 9], [4, 5, 8, 9], [4, 6, 7, 8], [4, 6, 7, 9], [4, 6, 8, 9], [4, 7, 8, 9], [5, 6, 7, 8], [5, 6, 7, 9], [5, 6, 8, 9], [5, 7, 8, 9], [6, 7, 8, 9]]    
   
    max_result = 1
    max_digit_set = []
    
    for numbers in lista:
        result_list = []
        for x in numbers:
            nums = numbers.copy()            
            nums.remove(x)
            compute(nums, x, result_list)
            result_list = sorted(set(result_list))


        if len(result_list) > max_result:
            consecutive = consecutive_int(result_list)
            if consecutive > max_result:
                max_result = consecutive
                max_digit_set = numbers.copy()
    
    print('{} {}'.format(max_result, max_digit_set))
    
solution()
