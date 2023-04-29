# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:32:25 2021

Problem 89: Roman numerals
https://projecteuler.net/problem=89

@author: Admin
"""
import time
from pathlib import Path

roman_nums = []

roman_dictonary = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def load_file(file_path):
    with open(file_path) as num:
        return num.read().splitlines()


def solution():
    file_path = Path(__file__).parent / "roman.txt"
    roman_nums = load_file(file_path)


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("Solution:", solution())
    print("Time:", time.time() - start_time)
