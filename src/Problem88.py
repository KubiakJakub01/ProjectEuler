# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:27:24 2021

Problem 88: Product-sum numbers
https://projecteuler.net/problem=88

@author: Admin
"""


import math

K = 12000
dict_k = {i: math.inf for i in range(2, K + 1)}

"""Progam taken from https://www.geeksforgeeks.org/print-combinations-factors-ways-factorize/"""


def factorsListFunc(first, each_prod, n, single_result_list):
    if first > n or each_prod > n:
        return

    if each_prod == n:
        diff = n - sum(single_result_list)
        k = diff + len(single_result_list)
        if k <= K and dict_k[k] > n:
            dict_k[k] = n
        return

    for i in range(first, n):
        if i * each_prod > n:
            break

        if n % i == 0:
            single_result_list.append(i)
            factorsListFunc(i, i * each_prod, n, single_result_list)
            single_result_list.remove(single_result_list[-1])


def factComb(n):
    single_result_list = []
    factorsListFunc(2, 1, n, single_result_list)


"""---------------------------------------------"""


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution():
    num = 4
    while sum(dict_k.values()) == math.inf:
        factComb(num)
        num += 1

    # print(dict_k)
    set_k = set(dict_k.values())
    # print('set: {} suma: {}'.format(set_k, sum(set_k)))
    print(sum(set_k))


solution()
