# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 21:53:45 2022

Problem 105: Special subset sums: testing
https://projecteuler.net/problem=105

@author: kuba
"""

'''
SOLUTION IDEA:
Krok 1:
    Wczytanie danych do listy w postaci: każdy set to osobna lista intów
Krok 2.0:
    Sprawdzenie pierwszego warunku dla wszystkich setów: 
    1. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
Krok 2.1:
    Wyznaczenie wszystkich możliwych kombinacji dla danych wielkosci zbiorów 
    (w tresci zadania jest podana informacja, ze zbiory są wielkosci od 7 do 12)
Krok 2.2:
    Wyznaczenie sum dla wszystkich dostępnych kombinacji setu i sprawdzenie czy jakas suma się powtarza,
    jesli tak to badany set nie spelnia warunki, w przeciwnym wypadku (żadna suma się nie powtarza), 
    set spełnia 1. warunek
Krok 3.0:
    Dla setów spełniających 1. warunek sprawdzenie 2. warunku:
    2. If B contains more elements than C then S(B) > S(C).
Krok 3.1:
    Wystarczy sprawdzić tylko "krytyczne" podziory tzn. dla posrtowanego rosnąco zbioru wystarczy brać pod uwagę:
    sumę "x+1" pierwszych elementów i "x" ostatnich elementów. Przykład: 
        A = [11, 18, 19, 20, 22, 25]
        x=1:
            11+18 > 25 +
        x=2:
            11+18+19>22+25 +            
    Jesli suma wszystkich podziobrów o większej licznosci jest większa to warunek 2. jest spełniony dla tego setu
Krok 4:
    Wyznaczenie sumy wszystkich setów, które spełniają obydwa warunku

Output:
    Wynik: 73702
--- 0.7921047210693359 seconds ---

Stopień trudnosci: 45%

'''

from itertools import combinations
from math import floor
import time

sets = []
temp_sets = []
with open('sets.txt') as file:
    temp_sets = file.readlines()
    
temp_sets = [x.strip().split(',') for x in temp_sets]

for s in temp_sets:
    sets.append(sorted([int(x) for x in s]))

temp_sets.clear()

def solution():
    result = 0
    combination_dict = {}
    for n in range(7,13):
        comb = []
        for i in range(1,n):
            comb += list(combinations(range(n), i))
        combination_dict[n] = comb
    
    for A in sets:
        flaga = True
        comb = combination_dict[len(A)]
        sumy = []
        
        for c in comb:
            suma = sum([A[x] for x in c])
            if sumy.count(suma):
                flaga = False
                break                
            sumy.append(suma)
            
        if flaga:
            index = 0
            flaga_2 = True
            
            A = sorted(A)
            if len(A)%2:
                index = floor(len(A)/2)+1
            else:
                index = floor(len(A)/2)
            
            for i in range(1, index):
                if sum(A[:i+1]) <= sum(A[-i:]):
                    flaga_2 = False
                    break
            if flaga_2:
                #print("Wynik: {}".format(A))
                result += sum(A)
                
    print('Wynik: {}'.format(result))
  
start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))

