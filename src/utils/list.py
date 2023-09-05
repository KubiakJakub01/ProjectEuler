"""Module for list utilities."""
from typing import List, Union, Generator


def is_palindromic(n: Union[int, str]) -> bool:
    """Check if a number is palindromic.

    Args:
        n (Union[int, str]): Number to check.

    Returns:
        bool: True if the number is palindromic, False otherwise.
    """
    return str(n) == str(n)[::-1]


def generate_powers(n: int) -> Generator[int]:
    """Generate a list of powers of 2 where the sum of last two numbers is less than n.

    Args:
        n (int): Number to check.

    Returns:
        List[int]: List of powers of 2.
    """
    suma_last_two = 0
    i = 1
    while suma_last_two < n:
        power = i**2
        i += 1
        suma_last_two = power + i**2
        yield power


def generate_palindromic_sums(n: int) -> Generator[int]:
    """Generate a list of palindromes that are the sum of consecutive squares.

    Args:
        n (int): Number to check.

    Returns:
        List[int]: List of palindromes that are the sum of consecutive squares.
    """
    power_list = list(generate_powers(n))
    for i in range(len(power_list)):
        suma = 0
        for j in range(i, len(power_list)):
            suma += power_list[j]
            if suma > n:
                break
            if j != i:
                if is_palindromic(suma):
                    yield suma


def generate_palindromic_sums_2(n: int) -> Generator[int]:
    """Generate a list of palindromes that are the sum of consecutive squares.

    Args:
        n (int): Number to check.

    Returns:
        List[int]: List of palindromes that are the sum of consecutive squares.
    """
    power_list = list(generate_powers(n))
    for i in range(len(power_list)):
        suma = 0
        for j in range(i, len(power_list)):
            suma += power_list[j]
            if suma > n:
                break
            if j != i:
                if is_palindromic(suma):
                    yield suma

