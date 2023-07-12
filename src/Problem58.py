# -*- coding: utf-8 -*-
"""
Problem 58 (Spiral primes)

Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. If this process is continued, 
what is the side length of the square spiral for which 
the ratio of primes along both diagonals first falls below 10%?
"""

import math


def solution():
    wynik = 1
    wielkosc_spirali = 3
    prime_on_corner = 3
    loop = 1
    corner_number = 5

    while wynik > 0.1:
        # for j in range(0, 3):
        wielkosc_spirali += 2
        for i in range(pow(wielkosc_spirali - 2, 2) + 1, pow(wielkosc_spirali, 2) + 1):
            if loop % (wielkosc_spirali - 1) == 0:
                corner_number += 1
                if is_prime(i):
                    # print("Pierwsza na cornerze: {}".format(i))
                    prime_on_corner += 1
            loop += 1
        wynik = prime_on_corner / corner_number
        loop = 1
    print("Wynik: {} {}".format(wielkosc_spirali, wynik))


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


solution()
