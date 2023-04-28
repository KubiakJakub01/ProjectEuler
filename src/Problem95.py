# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:29:30 2021

Problem 95: Amicable chains
https://projecteuler.net/problem=95

@author: kuba
"""

"""
chain: [14316, 19116, 31704, 47616, 83328, 177792, 295488, 629072, 
        589786, 294896, 358336, 418904, 366556, 274924, 275444, 243760, 
        376736, 381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 
        22744, 19916, 17716, 14316] 
        len: 28
"""

import math
import time

# Global
# Maximum value of numbers
limit = 10**6
dsums = [1] * limit


def searching_amicable_chain(prev_values, num):

    # if value was checked or value is prime num
    if num == 1:
        # we denote all value in this path
        for val in prev_values:
            dsums[val] = 1

    else:
        # checking is any cycle occurs in this path
        if prev_values.count(num):
            index = prev_values.index(num)
            len_of_chain = len(prev_values) - index

            # we denote all value in this path
            prev_values.append(num)
            print("chain: {} len: {}".format(prev_values[index:], len_of_chain))
            for val in prev_values:
                dsums[val] = 1

            return len_of_chain

        else:
            prev_values.append(num)
            new_num = dsums[num]

            return searching_amicable_chain(prev_values, new_num)


def solution():
    for i in range(2, limit):
        if i * i < limit:
            dsums[i * i] += i
        # Poor man's ceil operator
        ulimit = limit / i
        if limit % i != 0:
            ulimit += 1
        for k in range(i + 1, int(ulimit)):
            dsums[k * i] += k + i

    # print(len(dsums))
    for i, x in enumerate(dsums):
        if x > limit:
            dsums[i] = 1

    for x in dsums:
        if x != 1:
            searching_amicable_chain(prev_values=[], num=x)


start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
