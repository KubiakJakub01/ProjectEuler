# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:42:11 2020

Problem 76: Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

@author: Admin
"""


K = 100


def rek(num, n, ilosc=0):
    for x in range(1, n + 1):
        new_n = num - x
        if new_n == 0:
            # print('+1')
            ilosc += 1
            return ilosc
        else:
            ilosc = rek(new_n, x, ilosc=ilosc)

    return ilosc


def solution():
    count = 0
    for x in range(K - 1, 0, -1):
        temp = rek(K - x, x)
        count += temp

    print(count)


solution()
