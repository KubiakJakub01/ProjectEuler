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
    "M": "1000",
    "D": "500",
    "C": "100",
    "L": "50",
    "X": "10",
    "V": "5",
    "I": "1",
}


def load_file(file_path):
    with open(file_path) as num:
        return num.read().splitlines()


def roman_to_int(roman_num):
    return [roman_dictonary[x] for x in roman_num]


def group_numbers(int_nums):
    grouped_nums: list = []
    len_int_nums = list(map(len, int_nums))
    for element in sorted(set(len_int_nums), reverse=True):
        if element in len_int_nums:
            last_element = len(len_int_nums) - 1 - len_int_nums[::-1].index(element)
            grouped_nums.append(int_nums[:last_element + 1])
            int_nums = int_nums[last_element + 1:]
            len_int_nums = len_int_nums[last_element + 1:]
    return grouped_nums


def valid_grouped_nums(grouped_nums):
    def _valid_group(group):
        if len(group) > 3:
            return True
        else:
            return False
    valid_grouped_nums = []
    for group in grouped_nums:
        if len(group) > 3:
            valid_grouped_nums.append(group)
    return valid_grouped_nums


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
    grouped_int_nums_list = list(map(group_numbers, int_nums_list))
    for numer, grouped_int_nums in zip(roman_nums, grouped_int_nums_list):
        print(f"orginal: {numer} grouped: {grouped_int_nums}")
    # for roman, int_num, converted_roman in zip(roman_nums, int_nums_sum_list, converted_roman_nums):
    #     print(f"orginal: {roman} int: {int_num} converted: {converted_roman}")


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("Solution:", solution())
    print("Time:", time.time() - start_time)
