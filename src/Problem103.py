# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:53:18 2022

Problem 103: Special subset sums: optimum
https://projecteuler.net/problem=103

@author: kuba
"""

"""
SOLUTION IDEA:
Krok 1:
    Zastosować regułe wyznaczania optymalnego zbioru z tresci zadania 
Krok 2:
    Działa :)
Stopień trudnosci zadania: 45% 
"""

A_6 = [11, 18, 19, 20, 22, 25]
b = 20


def solution():
    A_7 = [b + A_6[i] for i in range(0, 6)]
    A_7.insert(0, b)

    # print(A_7)
    # print(sum(A_7))

    wynik = "".join([str(x) for x in A_7])
    print("Wynik: {}".format(wynik))


solution()
