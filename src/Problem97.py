# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:10:43 2021

Problem 97: Large non-Mersenne prime
https://projecteuler.net/problem=97

@author: kuba
"""


def solution():
    num = 2
    result = 0
    n = 7830457 + 1
    bufor = 10**10
    # temp_num = num
    for i in range(2, n):
        num *= 2
        num %= bufor

    # print('{}'.format(num))

    result = num * 28433 + 1
    result %= bufor
    print("wynik: {}".format(result))


solution()
