# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:32:25 2021

Problem 89: Roman numerals
https://projecteuler.net/problem=89

@author: Admin
"""
import time
from pathlib import Path

replacements = [
    ("VIIII", "IX"),
    ("IIII", "IV"),
    ("LXXXX", "XC"),
    ("XXXX", "XL"),
    ("DCCCC", "CM"),
    ("CCCC", "CD"),
]


def solution():
    pass

if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("Solution:", solution())
    print("Time:", time.time() - start_time)
