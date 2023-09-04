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
