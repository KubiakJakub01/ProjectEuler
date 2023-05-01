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


def load_file(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()


def solution():
    file_path = Path(__file__).parent / "roman.txt"
    roman_nums = load_file(file_path)
    saved_chars = 0
    for roman_num in roman_nums:
        saved_chars += len(roman_num)
        for old, new in replacements:
            roman_num = roman_num.replace(old, new)
        saved_chars -= len(roman_num)
    return saved_chars


if __name__ == "__main__":
    start_time = time.time()
    print("Solution:", solution())
    print("Time:", time.time() - start_time)
