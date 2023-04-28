# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:12:31 2021

Problem 65: Convergents of e
https://projecteuler.net/problem=65

@author: kuba
"""


def solution():
    e = []
    n = 2
    nums = [[2, 1], [3, 1]]

    while len(e) < 99:
        e.append(n)
        e.append(1)
        e.append(1)
        n += 2

    i = 1
    for x in e:
        numerator = nums[i][0] * x + nums[i - 1][0]
        dom = nums[i][1] * x + nums[i - 1][1]

        nums.append([numerator, dom])

        i += 1

    wynik = sum([int(x) for x in str(nums[99][0])])
    print(wynik)


solution()
