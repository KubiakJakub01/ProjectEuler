# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:23:07 2020

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

@author: Admin
"""





def solution():
    
    wynik = 0
    numbers = []
    power_lib = [pow(x,5) for x in range(0,10)]
    zakres = pow(10,5)*3
    
    for i in range(10,zakres):
        n = sorted(str(i))
        if numbers.count(n) == 0:
            numbers.append(n)
        
    #print(numbers)
            
    for num in numbers:
        #print(num)
        suma = [power_lib[int(y)] for y in num]
        liczba = sorted(str(sum(suma)))
        if liczba == num:
            wynik += sum(suma)
            
    print(wynik)
    #print(numbers)
    
           
solution()
