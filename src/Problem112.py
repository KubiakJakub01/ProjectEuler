# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 17:38:43 2022

Problem 112: Bouncy numbers
https://projecteuler.net/problem=112

@author: kuba
"""

"""
SOLUTION IDEA:
Krok 1:
    Wyznaczenie wszystkich 'non bouncy numbers'(nbn) mniejszych od danego N (N jest potęgą 10) 
    do czasu kiedy stosunek: 1-'nbn'/N < 99%
Krok 1.1:
    Non bouncy numbers dzielą się na rosnące i malejące. Rozpatrując grupę rosnąca do istniejącej już nbn
    wystarczyć dołożyć cyfrę niemniejszą od cyfry dziesiątek na pozycję dziesiętną (reszta cyfr się przesuwa).
    Analogicznie dla majejącej dodawane są mniejsze lub równe cyfry.
Krok 2:
    Aby okreslić liczbę N, dla której stosunek liczb 1-'nbn'/N == 0.9, obliczamy taki stosunek dla kolejnych
    'nbn' z wyznaczonego zbiori aż do czasu kiedy ten stosunek przekroczy 0.9 i wtedy wystarczy znalesc liczbę N
    z przedziału dla, której 1-'nbn'/N == 0.99 począwszy od poprzedniej 'non bouncy numbers'(która jeszcze nie 
                                                                                             przekroczyła progu
                                                                                             0.99)

Output:
    per: 0.99 n: 1587000
--- 0.02298569679260254 seconds ---

Stopień trudnosci: 15%
    
"""

import time


def solution():
    percent = 0.99
    current_percent = 0
    N = 100

    non_bouncy_nums = list(range(1, 10))
    increasing_nums = non_bouncy_nums.copy()
    decreasing_nums = non_bouncy_nums.copy()

    while current_percent < percent:
        temp_nums = []
        for n in increasing_nums:
            for i in range(n % 10, 10):
                num = n * 10 + i
                temp_nums.append(num)

        increasing_nums = temp_nums
        non_bouncy_nums += temp_nums

        temp_nums = []
        for n in decreasing_nums:
            for i in range(n % 10, -1, -1):
                num = n * 10 + i
                temp_nums.append(num)

        decreasing_nums = temp_nums
        non_bouncy_nums += temp_nums
        non_bouncy_nums = list(set(non_bouncy_nums))
        current_percent = 1 - (len(non_bouncy_nums) / N)
        N *= 10

    l = 0
    non_bouncy_nums = sorted(non_bouncy_nums)
    prev_num = 0
    for i in non_bouncy_nums:
        l += 1
        current_percent = 1 - (l / i)
        if current_percent >= percent:
            l -= 1
            for n in range(prev_num, i):
                current_percent = 1 - (l / n)
                if current_percent >= percent:
                    print("per: {} n: {}".format(current_percent, n))
                    break
            break
        prev_num = i


start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
