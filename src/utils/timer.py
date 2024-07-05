"""Module with timer utils"""
import time


def timer(func):
    """Timer decorator"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"--- {time.time() - start_time} seconds ---")
        return result

    return wrapper


def tqdm_timer(func):
    """Timer decorator with tqdm"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"--- {time.time() - start_time} seconds ---")
        return result

    return wrapper
