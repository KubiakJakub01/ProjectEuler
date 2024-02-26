# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:32:03 2021

Problem 46: Goldbach's other conjecture
https://projecteuler.net/problem=46

@author: kuba
"""


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution():
    prime_list = [2]
    flaga = True

    for i in range(3, 10000, 2):
        if not is_prime(i):
            for prime in prime_list:
                x = ((i - prime) / 2) ** (1 / 2)
                if x.is_integer():
                    flaga = True
                    break
        else:
            flaga = True
            prime_list.append(i)

        if not flaga:
            print(i)
            return 0

        flaga = False


solution()
