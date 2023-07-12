# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 00:15:29 2021

Problem 102: Triangle containment
https://projecteuler.net/problem=102

@author: kuba
"""


import numpy as np
import matplotlib.pyplot as plt

# Rysowanie przykładowych trójkątków
"""X = np.array([[-340,495], [-153,-910], [835, -947], [-175, 41], [-421, -714], [574, -645]])
Y = ['red', 'red', 'red', 'blue', 'blue', 'blue']

plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

t1 = plt.Polygon(X[:3,:], color=Y[0])
plt.gca().add_patch(t1)

t2 = plt.Polygon(X[3:6,:], color=Y[3])
plt.gca().add_patch(t2)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')"""

# plt.show()


# Reading from file
PATH_2_FILE = "triangles.txt"
bufor_list = []
triangles = []
with open(PATH_2_FILE) as p:
    bufor_list = p.readlines()

[triangles.append(x.strip().split(",")) for x in bufor_list]


def area(x1, y1, x2, y2, x3, y3):

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):

    # Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    A1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    A2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    A3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    if A == A1 + A2 + A3:
        return True
    else:
        return False


def solution():
    x = 0
    y = 0

    result = 0

    for triangle in triangles:
        x1 = int(triangle[0])
        y1 = int(triangle[1])
        x2 = int(triangle[2])
        y2 = int(triangle[3])
        x3 = int(triangle[4])
        y3 = int(triangle[5])

        if isInside(x1, y1, x2, y2, x3, y3, x, y):
            result += 1

    print(result)


solution()
