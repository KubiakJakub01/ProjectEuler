"""
Created on 03-01-2023 18:46

Problem 125: Palindromic sums
https://projecteuler.net/problem=125

@author: KubiakJakub01

Algorithm description:
    1. Create a list of powers of 2 where the sum of last two numbers is less than N
    2. Create nested loop where the first loop iterates over the list of powers of 2 
        and the second loop iterates over the list of powers of 2 starting from the first loop index
    3. Check if the sum of all numbers is palindromic
    4. Remove duplicates
    5. Print the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares
    6. END
"""
from .utils.timer import timer

N = 10**8


def generate_powers():
    # Create a list of powers of 2 where the sum of last two numbers is less than N
    power_list = []
    suma_last_two = 0
    i = 1
    while suma_last_two < N:
        power = i**2
        i += 1
        power_list.append(power)
        suma_last_two = power + i**2
    return power_list


def is_palindromic(n):
    # Check if a number is palindromic
    return str(n) == str(n)[::-1]


@timer
def solution():
    # Create a list of powers of 2 where the sum of all numbers is less than N
    power_list = generate_powers()

    # Create a list of palindromes that are the sum of consecutive squares
    palindrom_sum_list = []
    for i in range(len(power_list)):
        suma = 0
        for j in range(i, len(power_list)):
            suma += power_list[j]
            if suma > N:
                break
            if j != i:
                if is_palindromic(suma):
                    palindrom_sum_list.append(suma)
    # Remove duplicates
    palindrom_sum_list = list(set(palindrom_sum_list))

    # Print the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares
    print(sum(palindrom_sum_list))


if __name__ == "__main__":
    solution()

"""
--- 0.47824954986572266 seconds ---
"""
