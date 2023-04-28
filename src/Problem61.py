# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:47:27 2021

Problem 61: Cyclical figurate numbers
https://projecteuler.net/problem=61

@author: kuba
"""


def P(x, n):
    return {
        "3": int(n * (n + 1) / 2),
        "4": int(n**2),
        "5": int(n * (3 * n - 1) / 2),
        "6": int(n * (2 * n - 1)),
        "7": int(n * (5 * n - 3) / 2),
        "8": int(n * (3 * n - 2)),
    }[x]


def solution():
    numbers = dict()
    limit = 10**4

    for i in range(3, 9):
        n = 1
        i = str(i)

        while P(i, n) < 1000:
            n += 1

        tab = []
        l1 = []
        l2 = []
        while P(i, n) <= limit:
            num = str(P(i, n))
            l1.append(num[:2])
            l2.append(num[2:])
            n += 1

        tab.append(l1)
        tab.append(l2)

        numbers[i] = tab

    # print([len(numbers[str(i)]) for i in range(3,9)])
    # print(numbers['8'])

    initial_list = numbers["8"]
    remaining_numbers = numbers.copy()
    del remaining_numbers["8"]

    for i in range(0, len(initial_list[0])):
        initial_num = "".join(initial_list[0][i] + initial_list[1][i])
        # print('id: {} initial num: {}'.format(i, initial_num))
        find_num(
            searching_num=initial_list[1][i],
            nums=[initial_num],
            remaining_numbers=remaining_numbers,
        )


def find_num(searching_num="", nums=[], remaining_numbers=dict()):

    # print('nums: {} remaining keys: {}'.format(nums, remaining_numbers.keys()))

    # Check if we already have found our numbers
    # We used all avaliable triangle numbers from dictonary
    if len(remaining_numbers) == 0:
        # print('Here nums: {}'.format(nums))
        # Check if our last part of number is equal to initial num
        if searching_num == nums[0][:2]:
            suma = sum([int(x) for x in nums])

            print("Wynik: {}".format(nums))
            print("Sum: {}".format(suma))
            return

    # Loop through whole remaining keys in dictonary
    for key, number in remaining_numbers.items():
        for i, n in enumerate(number[0]):
            # If we found match element
            if n == searching_num:
                # Creating next step elements
                new_remaining_numbers = remaining_numbers.copy()
                del new_remaining_numbers[key]
                new_nums = nums.copy()
                new_searching_num = number[1][i]
                new_nums.append("".join(n + new_searching_num))

                find_num(
                    searching_num=new_searching_num,
                    nums=new_nums,
                    remaining_numbers=new_remaining_numbers,
                )

    return


solution()
