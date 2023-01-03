"""
Created on 03-01-2023 18:46

Problem 125: Palindromic sums
https://projecteuler.net/problem=125

@author: KubiakJakub01
"""

# import libraries
import time

N = 10**8

def solution():
    # Create a list of powers of 2 where the sum of all numbers is less than N
    power_list = []
    suma = 0
    i = 1
    while suma < N:
        power = i**2
        i += 1
        suma += power
        power_list.append(power)

if __name__ == "__main__":
    start_time = time.time()
    solution()
    print("--- %s seconds ---" % (time.time() - start_time))