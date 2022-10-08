# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:52:58 2022

Problem 111: Primes with runs
https://projecteuler.net/problem=111

@author: kuba
"""
import collections
from itertools import permutations

class PrimeRuns:
    m = 0
    n = 0
    s = 0
    digits = []

min_n = 10**1
max_n = 10**2
square = int(max_n**(1/2))+1

hh = list(range(0,square))
primes = list(range(min_n+1, max_n, 2)) 
N = len(primes)

def sieve():
    p = 3;
    while((p * p) < square):
        if (hh[p] != 0):
            for i in range((p * 2), square, p):
                hh[i] = 0;
        p += 1
    
    n = 0
    for h in list(set(hh))[2:]:
        #print('h: {}'.format(h))
        j=n
        while j<N: 
            if primes[j] != 0 and primes[j]%h == 0:
                break
            j+=1
            
        for i in range(j, N, h):
            #print('i: {} primes[i]: {}'.format(n+i, primes[i]))
            primes[i] = 0
        n+=1
    #print(set(primes))
    return list(set(primes))[1:]



def isPrime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True
 

def solution():
    wynik = 0
    primes = sieve()
    hh.clear()
    print(len(primes))
    
    primes_runs = [PrimeRuns() for i in range(0,10)]
    for prime in primes:
        coll = collections.Counter(str(prime)).most_common(1)[0]
        most_common = int(coll[0])
        count_most_common = coll[1]
        #print('count: {} m: {}'.format(count_most_common, primes_runs[most_common].m))
        if count_most_common > primes_runs[most_common].m:
            primes_runs[most_common].m = count_most_common
            primes_runs[most_common].n = 1
            primes_runs[most_common].s = prime
            primes_runs[most_common].digits = [prime]
        elif count_most_common == primes_runs[most_common].m:
            primes_runs[most_common].n += 1
            primes_runs[most_common].s += prime
            primes_runs[most_common].digits.append(prime)
    
            
    for i, runs in enumerate(primes_runs):
        print('d: {} m: {} n: {} s: {} \ndigits: {}'.format(i, runs.m, runs.n, runs.s, sorted(runs.digits)))
        wynik += runs.s
        print([isPrime(x) for x in runs.digits])
            
    print('Wynik: {}'.format(wynik))
            
#solution()


def f():
    #lista = [9*[x] for x in range(1,10)]
    lista = []
    for y in range(1,10):
        l = [9*[x]+[y] for x in range(1,10)]
        #l = l[0]
        lista += l
        #print(l)
        
        
    for l in lista[:3]:
        print(list(permutations(l)))

f()




