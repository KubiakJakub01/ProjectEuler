# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:27:40 2020

Problem 51: Prime digit replacements
By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, 
is part of an eight prime value family.

@author: Admin
"""

'''NIE SKONCZONE'''

def is_prime(n):
    for i in range(2,int(n**(1/2)+1)):
        if n%i==0: return False
    
    return True


def generate_prime_number(start, end):
    prime_numbers = []
    for num in range(start, end, 2):
        if is_prime(num): 
            prime_numbers.append(num)
        
    return prime_numbers


def solution():
    prime_numbers = []
    
    prime_numbers = generate_prime_number(101,1000)
    k = 3
    
    position = []
    for x in range(0,k):
        p = [str(num)[x] for num in prime_numbers]
        position.append(p)
        
    
    for j, tab in enumerate(position):  
        #print(tab)
        new_tab = [int(x) for x in tab]
        for i in range(0,10):
            count = new_tab.count(i)
            print('i= {} count= {}'.format(i,count))
            if count == 8:
                print('liczba: {} miejsce: {}'.format(i,j+1))
                

    
solution()