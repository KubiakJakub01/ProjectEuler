# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:50:47 2022

Problem 118: Pandigital prime sets
https://projecteuler.net/problem=118

@author: kuba
"""


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    pandigital_prime = []
    for i in range(2, n + 1):
        if prime[i] and str(i).count("0") == 0 and len(set(str(i))) == len(str(i)):
            pandigital_prime.append(str(i))
    prime.clear()
    return pandigital_prime


availability = {}
result = 0


def solution():
    n = 10**5
    prime = sieve_of_eratosthenes(n)
    for i, p in enumerate(prime):
        availability[p] = [
            x for x in prime[i:] if len(set(p).intersection(set(x))) == 0
        ]
    prime.clear()

    for item, value in availability.items():
        finding_pandigital_prime_sets(value=item, curr_set=[], intersection=set(value))
    print(result)


def finding_pandigital_prime_sets(value, curr_set, intersection):
    curr_set.append(value)

    if sum(len(s) for s in curr_set) == 9:
        # print(curr_set)
        global result
        result += 1
        return

    for next_value in intersection:
        next_intersection = intersection.intersection(set(availability[next_value]))
        # if len(curr_set)>=4:
        # print(f'curr_set: {curr_set} value: {value} next val: {next_value} intersection: {intersection} next_itersection: {next_intersection}')
        finding_pandigital_prime_sets(
            value=next_value, curr_set=curr_set.copy(), intersection=next_intersection
        )


solution()
