# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 00:15:29 2021

Problem 102: Triangle containment
https://projecteuler.net/problem=102

@author: kuba
"""


import numpy as np
import matplotlib.pyplot as plt


"""Plotting example
X = np.array([[-340,495], [-153,-910], [835, -947], [-175, 41], [-421, -714], [574, -645]])
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
ax.spines['right'].set_color('none')
"""


# Reading from file
PATH_2_FILE = "triangles.txt"
bufor_list = []
triangles = []
with open(PATH_2_FILE) as p:
    bufor_list = p.readlines()

[triangles.append(x.strip().split(",")) for x in bufor_list]


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    """Calculate area of triangle ABC

    Args:
        x1: x coordinate of point A
        y1: y coordinate of point A
        x2: x coordinate of point B
        y2: y coordinate of point B
        x3: x coordinate of point C
        y3: y coordinate of point C
        x: x coordinate of point P
        y: y coordinate of point P
    Returns:
        bool: True if point P lies inside the triangle ABC
    """

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

        if is_inside(x1, y1, x2, y2, x3, y3, x, y):
            result += 1

    print(result)


solution()
