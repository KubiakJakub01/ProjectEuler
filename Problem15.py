# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:42:28 2020

Problem 15: Lattice paths 

    Starting in the top left corner of a 2×2 grid, 
    and only being able to move to the right and down, 
    there are exactly 6 routes to the bottom right corner.
    
    How many such routes are there through a 20×20 grid?

@author: Admin
"""

def pascal_triangle(n):
    tab = [1,1]
    
    square_id = 1
    
    for x in range(1,n+1):
        if x%2 == 0:
            print('{}x{} - {}'.format(square_id,square_id,max(tab)))
            square_id += 1
            
        new_tab = [1]  
        
        for i in range(1,len(tab)):
            number = tab[i]+tab[i-1]
            new_tab.append(number)
            
        new_tab.append(1)
        tab = new_tab




def solution():
    n = 40
    pascal_triangle(n)
    
solution()


