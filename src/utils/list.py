"""Module for list utilities."""
from typing import List, Union, Generator, Callable

from tqdm import tqdm


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


def compute_solution(n: int) -> int:
    """Compute the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.

    Args:
        n (int): Number to check.

    Returns:
        int: Sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.
    """
    palindrom_sum_list = list(generate_palindromic_sums(n))
    return sum(palindrom_sum_list)


def compute_list_with_progress_bar(n: int) -> List[int]:
    """Compute the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.

    Args:
        n (int): Number to check.

    Returns:
        int: Sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.
    """
    palindrom_sum_list = []
    for i in tqdm(range(n)):
        palindrom_sum_list.append(compute_solution(i))
    return palindrom_sum_list


def compute_list(n: int, progress_bar: Callable = None) -> List[int]:
    """Compute the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.

    Args:
        n (int): Number to check.
        progress_bar (Callable, optional): Progress bar function. Defaults to None.

    Returns:
        int: Sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.
    """
    palindrom_sum_list = []
    for i in range(n):
        palindrom_sum_list.append(compute_solution(i))
        if progress_bar is not None:
            progress_bar(i, n)
    return palindrom_sum_list


def write_to_file(n: int, file_name: str) -> None:
    """Write the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares to a file.

    Args:
        n (int): Number to check.
        file_name (str): Name of the file.
    """
    with open(file_name, "w") as file:
        for i in range(n):
            file.write(f"{compute_solution(i)}\n")


def load_from_file(file_name: str) -> List[int]:
    """Load the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares from a file.

    Args:
        file_name (str): Name of the file.

    Returns:
        List[int]: List of sums.
    """
    with open(file_name, "r") as file:
        return [int(line) for line in file.readlines()]


def load_with_fn(file_name: str, fn: Callable) -> List[int]:
    """Load the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares from a file.

    Args:
        file_name (str): Name of the file.
        fn (Callable): Function to apply to each line.

    Returns:
        List[int]: List of sums.
    """
    with open(file_name, "r") as file:
        return [fn(line) for line in file.readlines()]


def graph_list(n: int, file_name: str) -> None:
    """Graph the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.

    Args:
        n (int): Number to check.
        file_name (str): Name of the file.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(n), load_from_file(file_name))
    plt.show()


def print_list(n: int, file_name: str) -> None:
    """Print the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.

    Args:
        n (int): Number to check.
        file_name (str): Name of the file.
    """
    print(load_from_file(file_name))


def plot_list(n: int, file_name: str) -> None:
    """Plot the sum of all the numbers that are both palindromic and can be written as the sum of consecutive squares.

    Args:
        n (int): Number to check.
        file_name (str): Name of the file.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(np.arange(n), load_from_file(file_name))
    plt.show()
