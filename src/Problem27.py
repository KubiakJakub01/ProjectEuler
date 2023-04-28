# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:31:40 2021

Problem 27: Quadratic primes
https://projecteuler.net/problem=27

@author: kuba
"""

import numpy as np


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution():
    prime_n = []
    wynik = 0
    iloczyn = 0
    for x in range(2, 1000):
        if is_prime(x):
            prime_n.append(x)

    # print(prime_n)

    for b in prime_n:
        for a in range(-999, 1000, 2):
            count = 0
            for i in range(0, 80):
                n = i**2 + a * i + b
                if n > 0 and is_prime(n):
                    count += 1
                else:
                    break

            if count > wynik:
                wynik = count
                iloczyn = a * b
                print("a: {} b: {}".format(a, b))

    print("Wynik: {} iloczyn: {}".format(wynik, iloczyn))


solution()
