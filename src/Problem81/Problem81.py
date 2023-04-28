# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 23:05:27 2021

Problem 81: Path sum: two ways
https://projecteuler.net/problem=81

@author: Admin
"""

import numpy as np

# Loading matrix(80x80)
"""matrix = [[131, 673, 234, 103, 18],
          [201, 96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537,699,497,121,956],
          [805,732,524,37,331]]"""

matrix = []
size = 80

with open("matrix.txt") as file:
    matrix = file.readlines()

matrix = [x.strip().split(",") for x in matrix]


def solution():

    min_path_matrix = np.zeros((size, size))
    rek(x=0, y=0, suma=0, min_path_matrix=min_path_matrix)
    print(min_path_matrix[-1][-1])


def rek(x, y, suma, min_path_matrix):
    suma += int(matrix[x][y])
    flag_go = False
    if min_path_matrix[x][y] == 0:
        min_path_matrix[x][y] = suma
        flag_go = True

    elif min_path_matrix[x][y] > suma:
        min_path_matrix[x][y] = suma
        flag_go = True

    if flag_go:
        if x < size - 1:
            x_1 = x + 1
            rek(x_1, y, suma, min_path_matrix)
        if y < size - 1:
            y_1 = y + 1
            rek(x, y_1, suma, min_path_matrix)
    return


solution()
