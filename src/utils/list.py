"""Module for list utilities."""
from typing import List, Union


def is_palindromic(n: Union[int, str]) -> bool:
    """Check if a number is palindromic.

    Args:
        n (Union[int, str]): Number to check.

    Returns:
        bool: True if the number is palindromic, False otherwise.
    """
    return str(n) == str(n)[::-1]
