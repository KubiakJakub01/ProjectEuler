# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 21:24:25 2021

Problem 59: XOR decryption
https://projecteuler.net/problem=59

@author: kuba
"""

# Importing encrypted values
PATH_TO_KEYS = "keys.txt"
encrypted_values = []
with open(PATH_TO_KEYS) as p:
    encrypted_values = p.readlines()

encrypted_values = encrypted_values[0]
encrypted_values = encrypted_values.replace(",", " ").split()


def most_common(lst):
    return max(set(lst), key=lst.count)


def solution():
    list_of_encrypted_val = []
    result = 0

    # Split encrypted num for 3 list for each value of key
    for i in range(0, 3):
        list_of_encrypted_val.append(
            [int(encrypted_values[j]) for j in range(i, len(encrypted_values), 3)]
        )

    # Looking for key
    for encrypted in list_of_encrypted_val:
        common_decoded_val = []
        for x in encrypted:
            decoded = [x ^ i for i in range(97, 123)]
            common_decoded_val += set(decoded)
        # Take most common value
        key = most_common(common_decoded_val)
        result += sum([v ^ key for v in encrypted])

    print(result)


solution()
