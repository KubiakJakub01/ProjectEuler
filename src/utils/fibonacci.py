"""
Module for Fibonacci sequence
"""


def fib(n: int) -> int:
    """Return the nth Fibonacci number:

    Args:
        n (int): The index of the Fibonacci number to return

    Returns:
        int: The nth Fibonacci number"""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        # Iterative solution
        # https://en.wikipedia.org/wiki/Fibonacci_number
        # https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
        # https://www.youtube.com/watch?v=Qk0zUZW-U_M
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
    

def fib_recursive(n: int, result_dict: dict = None) -> int:
    """Return the nth Fibonacci number:
    
    Args:
        n (int): The index of the Fibonacci number to return
        result_dict (dict): A dictionary to store already calculated results
    
    Returns:
        int: The nth Fibonacci number"""
    if n < 0:
        raise ValueError("n must be >= 0")
    if result_dict is None:
        result_dict = {}
    if n in result_dict:
        return result_dict[n]
    if n == 0:
        result_dict[n] = 0
        return 0
    if n == 1:
        result_dict[n] = 1
        return 1
    else:
        result_dict[n] = fib_recursive(n - 1, result_dict) + fib_recursive(n - 2, result_dict)
        return result_dict[n]


if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number is {fib(n)}")


def fib_recursive(n: int, result_dict: dict = None) -> int:
    """Return the nth Fibonacci number:
    
    Args:
        n (int): The index of the Fibonacci number to return
        result_dict (dict): A dictionary to store already calculated results
    
    Returns:
        int: The nth Fibonacci number"""
    if n < 0:
        raise ValueError("n must be >= 0")
    if result_dict is None:
        result_dict = {}
    if n in result_dict:
        return result_dict[n]
    if n == 0:
        result_dict[n] = 0
        return 0
    if n == 1:
        result_dict[n] = 1
        return 1
    else:
        result_dict[n] = fib_recursive(n - 1, result_dict) + fib_recursive(n - 2, result_dict)
        return result_dict[n]
