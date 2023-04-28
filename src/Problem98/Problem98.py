# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:32:22 2021

Problem 98: Anagramic squares
https://projecteuler.net/problem=98

@author: kuba
"""

""" 
SOLUTION IDEA:
Krok 1:
    Wczytanie danych do listy    
Krok 2:
    Zgrupowanie danych w taki sposób aby w danej grupie znalazły się słowa, które są swoimi anagramami,
    tzn. są stworzone z dokładnie tych samych liter i mają tą samą długosc
Krok 3:
    Wyznaczenie zbioru par licz, które spełniają założenia problemu. tzn. są swoimi anagramami 
    i obydwie liczby są potęgami liczb całkowitych. Dodatkowo zbiór dla ułatwienia operacji jest pogrupowany
    względem długosci i maksymalna długosc liczb wynosi 5
Krok 4:
    Dla każdego z zbioru stworzonego w kroku 2 par słów porównanie odpowiedniego (względem długosci słowa)
    podzbioru wygenerowanych możliwych par potęgo z kroku 3. Sprawdzenie czy dana para liczb i słów 'pasuję' 
    do siebie wyglada następująco:
        - parę słów i parę liczb dzieli się na dwa oddzielne (1 i 2)
        - na podstawie pierwszego słowa i liczby przypisuje się literę do cyfry
        - następnie dla słowa nr 2 następuje zamiana znaku na odpowiednią cyfrę
        - aby uniknąć problemu z przypysaniem tej samj cyfry do dwóch różnych liter, przed zamianą w drugim słowie
            sprawdza się czy: dana litera jest jescze w słowie i czy odpowiednia cyfra nie została juz wpisana
        - na koniec przerobionę słowo nr 2 porównuje się z liczbą nr 2, jesli są takie same tzn. że dana para
            spełnia warunki zadania
        - do uzyskania wyniku brana jest maksymalna licza z zbioru par liczb, które spełniają warunki

Output:
    Wynik: 18769
--- 0.08694791793823242 seconds ---

Stopień trudnosci: 35%

"""

import numpy as np
import collections
from itertools import permutations
import time

PATH_2_FILE = "words.txt"
words_list = []
with open(PATH_2_FILE) as file:
    words_list = file.readlines()

words_list = words_list[0].split(",")
words_list = [x[1:-1] for x in words_list]

powers = {}
grouped_list = []
MAX_LEN = 5


def find_squares():
    numbers = []
    size = 0
    N = 10**3
    for i in range(10, N):
        numbers.append(i)
        power = str(i**2)
        if len(power) > MAX_LEN:
            break
        # anagram_i = int(str(i)[::-1])
        if size != len(power):
            size = len(power)
            powers[size] = []
            numbers = []

        # anagram_power = str(anagram_i**2)
        permutacje = set(list(permutations(power)))

        for perm in permutacje:
            n = int("".join(perm))
            sqrt = (n) ** (1 / 2)
            if sqrt.is_integer():
                n = str(n)
                sqrt = int(sqrt)
                if len(power) == len(n) and power != n and numbers.count(sqrt) == 0:
                    numbers.append(sqrt)
                    pair = [power, n]
                    powers[size].append(pair)


# find_squares()


def solution():
    dcit_of_words = collections.defaultdict(list)
    results = []

    for word in words_list:
        dcit_of_words[len(word)].append(word)

    del dcit_of_words[1]

    for key, value in dcit_of_words.items():
        value_copy = ["".join(sorted(x)) for x in value]

        for val in value_copy:
            group_list = []
            # indices = list(filter(lambda x: x == val, value_copy))
            if val != 0:
                index_list = [i for i, x in enumerate(value_copy) if x == val]

                if len(index_list) > 1:
                    for i in index_list:
                        value_copy[i] = 0
                        group_list.append(value[i])

                    grouped_list.append(group_list)

    find_squares()
    i = 1
    for group in grouped_list:
        if len(group) == 2 and len(group[0]) <= MAX_LEN and len(group[0]) > 2:
            word_1 = group[0]
            for nums in powers[len(word_1)]:
                word = group[1]
                num_1 = nums[0]
                num_2 = nums[1]
                for i in range(0, len(num_1)):
                    if word.count(word_1[i]) != 0 and word.count(num_1[i]) == 0:
                        word = word.replace(word_1[i], num_1[i])
                    else:
                        break

                if word == num_2:
                    # print('{} {} word: {}'.format(group, nums, word))
                    results.append(int(num_1))
                    results.append(int(num_2))

    print("Wynik: {}".format(max(results)))


start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))
