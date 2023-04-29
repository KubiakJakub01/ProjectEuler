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


def roman_to_int(roman_num):
    return [roman_dictonary[x] for x in roman_num]


def sum_int_nums(int_nums):
    sum = 0
    for i in range(len(int_nums)):
        if i + 1 < len(int_nums) and int_nums[i] < int_nums[i + 1]:
            sum -= int_nums[i]
        else:
            sum += int_nums[i]
    return sum


def int_to_roman(int_num):
    roman_num = ""
    for key, value in roman_dictonary.items():
        while int_num >= value: 
            roman_num += key
            int_num -= value
    return roman_num


def solution():
    file_path = Path(__file__).parent / "roman.txt"
    roman_nums = load_file(file_path)
    int_nums_list = list(map(roman_to_int, roman_nums))
    int_nums_sum_list = list(map(sum_int_nums, int_nums_list))
    converted_roman_nums = list(map(int_to_roman, int_nums_sum_list))
    for roman, int_num, converted_roman in zip(roman_nums, int_nums_sum_list, converted_roman_nums):
        print(f"orginal: {roman} int: {int_num} converted: {converted_roman}")


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("Solution:", solution())
    print("Time:", time.time() - start_time)
