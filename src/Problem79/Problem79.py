# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:52:26 2021

Problem 79: Passcode derivation
https://projecteuler.net/problem=79

@author: Admin
"""

keylog = []

with open("keylog.txt") as keys:
    keylog = keys.readlines()


keylog = [x.strip() for x in keylog]


def solution():
    unique_num = sorted(set("".join(keylog)))
    dict_of_num = dict.fromkeys(unique_num, "")

    for key in keylog:
        dict_of_num[key[0]] += key[1:]
        dict_of_num[key[1]] += key[2]

    for i, val in dict_of_num.items():
        dict_of_num[i] = len(set(val))

    result = dict(
        sorted(dict_of_num.items(), key=lambda item: item[1], reverse=True)
    ).keys()
    print("".join(result))


solution()
