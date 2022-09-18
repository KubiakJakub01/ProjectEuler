# -*- coding: utf-8 -*-
"""
Created on 17-09-2022 10:17

Problem 96: Su Doku
https://projecteuler.net/problem=96

@author: Jakub

Algoritm description draft:
    1. Read the file
    2. Create a list of sudoku
    3. Solve the sudoku:
        3.1 Check if the sudoku is solved
        3.2 If not, determine aviailable numbers for each cell
        3.3 Fill the cells with only one available number
        3.4 If there is no cell with only one available number, guess the number
        3.5 Repeat 3.1-3.4 until the sudoku is solved
    4. Return the sum of the 3-digit numbers found in the top left corner of each solved sudoku
"""

# import libraries
import numpy as np

SUDOKU_PATH = 'Problem96\sudoku.txt'
# function to read the file
def read_file():
    with open(SUDOKU_PATH) as f:
        sudoku_list = f.read().split('Grid ')
    # 2. Create a list of sudoku
    sudoku_list = [x.splitlines()[1:] for x in sudoku_list[1:]]
    # list of strings to 2d array of ints
    sudoku_array = [np.array([list(map(int, x)) for x in sudoku])
                    for sudoku in sudoku_list]
    return sudoku_array

# function to check if the sudoku is solved
def is_solved(sudoku):
    if sudoku is False or 0 in sudoku:
        return False
    else:
        # check if sudo is valid
        for i in range(9):
            if len(np.unique(sudoku[i, :])) != 9:
                return None
            if len(np.unique(sudoku[:, i])) != 9:
                return None
        for i in range(3):
            for j in range(3):
                square = sudoku[3*i:3*i+3, 3*j:3*j+3]
                if len(np.unique(square)) != 9:
                    return None
    return True

# function to determine available numbers for each cell
def determine_available_numbers_for_cell(sudoku, i, j):
    available_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # check row
    available_numbers = available_numbers[~np.isin(
        available_numbers, sudoku[i, :])]
    # check column
    available_numbers = available_numbers[~np.isin(
        available_numbers, sudoku[:, j])]
    # check square
    square = sudoku[3*(i//3):3*(i//3)+3, 3*(j//3):3*(j//3)+3]
    available_numbers = available_numbers[~np.isin(available_numbers, square)]
    # padded with zeros to have the same shape as sudoku
    padded_available_numbers = np.zeros(9)
    padded_available_numbers[available_numbers-1] = available_numbers
    return padded_available_numbers

# function to determine available numbers for each cell
def determine_available_numbers(sudoku):
    available_numbers = np.zeros((9, 9, 9))
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                available_numbers[i, j, :] = determine_available_numbers_for_cell(
                    sudoku, i, j)
    return available_numbers

# function to fill the cells with only one available number
def fill_cells_with_one_available_number(sudoku, available_numbers):
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0 and np.count_nonzero(available_numbers[i, j, :]) == 1:
                sudoku[i, j] = available_numbers[i, j, :][available_numbers[i, j, :] != 0]
    return sudoku


# function to find the cell with least aviable number
def find_cell_with_least_available_numbers(sudoku, available_numbers):
    min_number_of_available_numbers = 10
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0 and np.count_nonzero(available_numbers[i, j, :]) < min_number_of_available_numbers:
                min_number_of_available_numbers = np.count_nonzero(
                    available_numbers[i, j, :])
                min_i = i
                min_j = j

    #print('min number of available numbers: ', min_number_of_available_numbers)
    return min_i, min_j, min_number_of_available_numbers


# function to solve the sudoku
def solve_sudoku(sudoku):
    min_number_of_available_numbers = 1

    if is_solved(sudoku):
        return sudoku

    # check if sudoku is solved or is any aviable number
    while min_number_of_available_numbers == 1:
        available_numbers = determine_available_numbers(sudoku)
        sudoku = fill_cells_with_one_available_number(sudoku, 
                                                    available_numbers)
        # check if sudoku is solved
        is_solved_or_valid = is_solved(sudoku)
        # if solved
        if is_solved_or_valid == True:
            return sudoku
        # if solved but not valid
        elif is_solved_or_valid == None:
            return False
        # if not solved but valid
        else:
            available_numbers = determine_available_numbers(sudoku)
            min_i, min_j, min_number_of_available_numbers = find_cell_with_least_available_numbers(sudoku, 
                                                                                            available_numbers)
    if min_number_of_available_numbers == 0:
        return False

    elif not is_solved(sudoku):
        # try to solve sudoku with each aviable number
        for number in available_numbers[min_i, min_j, :]:
            if number != 0:
                temp_sudoku = sudoku.copy()
                temp_sudoku[min_i, min_j] = number
                temp_sudoku = solve_sudoku(temp_sudoku)
                if is_solved(temp_sudoku):
                        return temp_sudoku
    return sudoku


# main solution function
def solution():
    # 1. Read the file
    sudoku_array = read_file()
    result = 0
    # 3. Solve the sudoku:
    for i, sudoku in enumerate(sudoku_array):
        sudoku = solve_sudoku(sudoku)
        print('##############################################')
        print(f'solved sudoku nr: {i}\n{sudoku}')
        print('##############################################')
        result += sudoku[0, 0]*100 + sudoku[0, 1]*10 + sudoku[0, 2]
    # 4. Return the sum of the 3-digit numbers found in the top left corner of each solved sudoku
    return result


if __name__ == '__main__':
    print(solution())