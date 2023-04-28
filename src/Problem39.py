# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:05:58 2021

Problem 39: Integer right triangles
https://projecteuler.net/problem=39

@author: kuba
"""

import time


def most_common(lst):
    return max(set(lst), key=lst.count)


def solution():
    wynik = 0
    perimeter_list = []
    for a in range(1, 500):
        for b in range(1, a + 1):
            c = (a**2 + b**2) ** (1 / 2)
            if c.is_integer():
                permiter = a + b + c
                if permiter <= 1000:
                    perimeter_list.append(permiter)
                else:
                    break

    # lista = [[x, perimeter_list.count(x)] for x in set(perimeter_list)]
    m_common = most_common(perimeter_list)
    # print(perimeter_list.count(120))
    # print(lista)
    # print('most common {} ilosc: {}'.format(m_common, perimeter_list.count(m_common)))
    print(m_common)


start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
