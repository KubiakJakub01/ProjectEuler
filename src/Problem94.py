# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:35:31 2021

Problem 94: Almost equilateral triangles
https://projecteuler.net/problem=94

@author: kuba
"""

"""
triangle 1: (5.0 5.0 6.0) h: 4
triangle 2: (17.0 17.0 16.0) h: 15
triangle 1: (65.0 65.0 66.0) h: 56
triangle 2: (241.0 241.0 240.0) h: 209
triangle 1: (901.0 901.0 902.0) h: 780
triangle 2: (3361.0 3361.0 3360.0) h: 2911
triangle 1: (12545.0 12545.0 12546.0) h: 10864
triangle 2: (46817.0 46817.0 46816.0) h: 40545
triangle 1: (174725.0 174725.0 174726.0) h: 151316
triangle 2: (652081.0 652081.0 652080.0) h: 564719
triangle 1: (2433601.0 2433601.0 2433602.0) h: 2107560
triangle 2: (9082321.0 9082321.0 9082320.0) h: 7865521
triangle 1: (33895685.0 33895685.0 33895686.0) h: 29354524
triangle 2: (126500417.0 126500417.0 126500416.0) h: 109552575
518408346.0
"""

import math

# Square equesion solver
def square_equesion_solver(a, b, c):
    delta = b**2 - (4 * a * c)

    if delta > 0:
        delta = delta ** (1 / 2)

        x_1 = (-b - delta) / (2 * a)
        x_2 = (-b + delta) / (2 * a)

        # print('x_1: {} x_2: {}'.format(x_1, x_2))

        if x_1.is_integer() and x_1 > 0:
            return x_1
        elif x_2.is_integer() and x_2 > 0:
            return x_2

    return 0


def solution():

    N = 10**9

    max_x = N / 2

    total_permiters = 0
    h = 4
    h_1 = 15

    while h < max_x and h_1 < max_x:
        c = -1 - (h * 2) ** 2
        x_1 = square_equesion_solver(3, -2, c)
        c = -1 - (h_1 * 2) ** 2
        x_2 = square_equesion_solver(3, 2, c)

        if x_1 != 0:
            print("triangle 1: ({} {} {}) h: {}".format(x_1, x_1, x_1 + 1, h))

            total_permiters += 3 * x_1 + 1

            h = math.floor(h * 13.9 / 4) * 4

        if x_2 != 0:
            print("triangle 2: ({} {} {}) h: {}".format(x_2, x_2, x_2 - 1, h_1))
            total_permiters += 3 * x_2 - 1

            h_1 = math.floor(h_1 * 13.9 / 2) * 2 - 1

        h += 4
        h_1 += 2

    print(total_permiters)


solution()
