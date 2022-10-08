# -*- coding: utf-8 -*-
"""
Created on 24-09-2022 17:09

Problem 101: Optimum polynomial
https://projecteuler.net/problem=101

@author: Jakub

Algoritm description [draft]:
    1. Create a list of points
    2. Create a list of polynomials
    3. Check if the polynomial is correct
    4. END
"""

# import libraries
import time
import numpy as np

# given coefficients:  
# 1 − n + n2 − n3 + n4 − n5 + n6 − n7 + n8 − n9 + n10
COEFFICIENTS = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
TEST_COEFFICIENTS = [0, 0, 0, 1]
N = 10

# polunomial function
def polynomial(x, coefficients):
    result = coefficients[0]
    for i in range(1, len(coefficients)):
        result += coefficients[i] * x ** i
    return result

# main solution function
def solution():
    b = []
    BOP = []    
    for x in range(1, N+1):
        coefficients_metrix = []
        for n in range(1, x+1):
            coefficients_metrix.append([n ** m for m in range(0, x)])
        a = np.array(coefficients_metrix)
        b.append(polynomial(x, COEFFICIENTS))        
        X = np.linalg.solve(a, b)
        BOP.append(int(polynomial(x+1, X)))
    return BOP
    
if __name__ == "__main__":
    #start_time = time.time()
    BOP = solution()
    print(f'BOP: {BOP} sum: {sum(BOP)}')
    #print("--- %s seconds ---" % (time.time() - start_time))
    '''a = np.array([[1, 1, 1], [1, 2, 4], [1, 3, 9]])
    b = np.array([1, 8, 27])
    x = np.linalg.solve(a, b)
    print(x)'''
