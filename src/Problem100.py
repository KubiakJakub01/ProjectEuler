# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:03:27 2021

Problem 100: Arranged probability
https://projecteuler.net/problem=100

@author: Admin
"""

import math


def solution():

    blue = 85
    red = 35

    n = 20
    limit = 10**5
    coff = 5.7

    # for n in range(20,10000):
    while n < limit:
        i = math.floor(n * 0.7)
        result = 0
        while result < 0.5:
            result = (i * (i - 1)) / (n * (n - 1))

            if result == 0.5:
                # print('{}/{} * {}/{} == 0.5'.format(i,n,i-1,n-1))

                print("{}*{}/{}*{}".format(i, i - 1, n, n - 1))
                n = int(n * coff)

            i += 1

        n += 1


# solution()

import numpy as np

symbols = ["0", "#"]


def generate_maze(X, Y):
    rate = 0.25  # the probability of the appearance of a wall
    temp_maze = np.random.choice(symbols, (X, Y), p=[1 - rate, rate])
    temp_maze[0][0] = "*"

    maze = []
    for m in temp_maze:
        maze.append("".join(m))
    return maze


generate_maze(5, 5)
