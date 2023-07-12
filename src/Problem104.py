# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:26:53 2021

Problem 104: Pandigital Fibonacci ends
https://projecteuler.net/problem=104

@author: kuba
"""


def solution():
    flag = True
    liczba_begin = 0
    liczba_end = 0
    liczba_str_begin = ""
    liczba_str_end = ""

    n_begin = [1, 1]
    n_end = [1, 1]
    i = 2

    while flag:
        liczba_begin = n_begin[0] + n_begin[1]
        liczba_str_begin = str(liczba_begin)[:9]

        liczba_end = n_end[0] + n_end[1]
        liczba_str_end = str(liczba_end)[-9:]

        i += 1

        if (liczba_str_end.count("0") == 0) and len(set(liczba_str_end)) == 9:
            if (liczba_str_begin.count("0") == 0) and len(set(liczba_str_begin)) == 9:
                flag = False

        # liczba_begin = int(str(liczba_begin)[:55])
        n_begin[0] = n_begin[1]
        n_begin[1] = liczba_begin

        liczba_end = int(liczba_str_end)
        n_end[0] = n_end[1]
        n_end[1] = liczba_end

        # print(i)

    print(
        "Liczba begin: {} liczba end: {} i: {}".format(liczba_str_begin, liczba_end, i)
    )


solution()
