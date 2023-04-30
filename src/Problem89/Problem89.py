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
        group_len_list = list((map(len, group)))
        group_num_with_frequency = {x: group.count(x) for x in group}
        group_string = "".join(group)
        if len(group) == 1:
            return True
        if group_string.count("5") > 1:
            return False
        if max(group_len_list) == min(group_len_list):
            # Get the most frequent element
            if max(group_num_with_frequency.values()) >= 4 and max(group_num_with_frequency.keys()) != "1000":
                return False
            return True
        if group_len_list[-2] == str(min(group_len_list)) and group_string.count(min(group_len_list)) == 1:
            return True
        return True
    return list(map(_valid_group, grouped_nums))


def int_to_roman(int_num):
    roman_num = ""
    for key, value in roman_dictonary.items():
        while int_num >= value: 
            roman_num += key
            int_num -= value
    return roman_num


def get_saved_chars(roman_num):
    int_num = int("".join(roman_num))
    converted_roman_num = int_to_roman(int_num)
    return len(roman_num) - len(converted_roman_num)


def solution():
    file_path = Path(__file__).parent / "roman.txt"
    roman_nums = load_file(file_path)
    int_nums_list = list(map(roman_to_int, roman_nums))
    grouped_int_nums_list = list(map(group_numbers, int_nums_list))
    for numer, grouped_int_nums in zip(roman_nums, grouped_int_nums_list):
        print(f"orginal: {numer} grouped: {grouped_int_nums} valid: {valid_grouped_nums(grouped_int_nums)}")


if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("Solution:", solution())
    print("Time:", time.time() - start_time)
