# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:20:36 2021

Problem 96: https://projecteuler.net/problem=96

@author: Admin
"""

import numpy as np

FULL_SET = ['1','2','3','4','5','6','7','8','9']
GRID_SIZE = 9


lines = []

with open('sudoku.txt') as s:
    lines = s.readlines()

lines = [list(x.strip()) for x in lines]

sudoku_list = []

for i in range(1,500,10):
    sudoku = np.array(list(lines[i:i+GRID_SIZE])).reshape((GRID_SIZE,GRID_SIZE))
    sudoku_list.append(sudoku)
    


def solution():
    RESULT = 0
    
    for sudoku in sudoku_list:
        number_of_zero = np.count_nonzero(sudoku == '0')
        print('sudoku: \n {} \n liczba zer = {}'.format(sudoku, number_of_zero))
        while number_of_zero != 0:      
            for x in range (0,GRID_SIZE):  
                box_x = (x//3)*3
                for y in range (0,GRID_SIZE):
                    if sudoku[x][y] == '0':
                        box_y = (y//3)*3
                        unique_val = FULL_SET
                        #Check row
                        #print('{} - {}'.format(unique_val,sudoku[x]))
                        unique_val = list(set(unique_val) - set(sudoku[x]))
                        #Check column
                        #print('{} - {}'.format(unique_val, sudoku[:,y]))
                        unique_val = list(set(unique_val) - set(sudoku[:,y]))
                        #Check box
                        #print('{} - {}'.format(set(unique_val), set(sudoku[box_x:box_x+3, box_y:box_y+3].flatten())))
                        unique_val = list(set(unique_val) - set(sudoku[box_x:box_x+3, box_y:box_y+3].flatten()))
                        
                        
                        #print('unique val: {} x: {} y: {}'.format(unique_val,x,y))
                        if len(unique_val) == 1:                      
                            sudoku[x][y] = str(unique_val[0])
                            number_of_zero -= 1
                            #print('Zmiana na: {}'.format(unique_val[0]))
            print('sudoku: \n {} \n liczba zer = {}'.format(sudoku, number_of_zero))
            wait = input() 
                            
        RESULT += int(''.join(sudoku[0][:3]) )              
       
    print(RESULT)

solution()


