"""Module with timer utils"""
import time

from tqdm import tqdm


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


if __name__ == "__main__":

    @timer
    def test():
        """Test function"""
        time.sleep(1)
        return "test"

    print(test())
