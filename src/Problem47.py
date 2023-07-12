# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:53:23 2021

Problem 47: Distinct primes factors
https://projecteuler.net/problem=47

@author: kuba
"""


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution():
    prime_list = [2]
    global_count = 0

    for i in range(3, 200000):
        count = 0
        if is_prime(i) and i < 1000:
            prime_list.append(i)
        else:
            n = i
            for p in prime_list:
                if n == 1:
                    break
                elif n % p == 0:
                    while n % p == 0:
                        n = n / p
                    count += 1
                    if count >= 5:
                        break

        if count == 4:
            # print(i)
            global_count += 1
            if global_count == 4:
                print(i - 3)
                return 0
        else:
            global_count = 0


solution()
