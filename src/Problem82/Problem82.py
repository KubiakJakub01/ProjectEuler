"""
Created on 22.07.2023 12:50

Problem 82: Path Sum: Three Ways
https://projecteuler.net/problem=82

author: KubiakJakub01
"""
# import libraries
import time
import math
from pathlib import Path

import numpy as np

MATRIX_FILE = Path(__file__).parent / "matrix.txt"


def solution():
    # read matrix from file
    matrix = np.loadtxt(MATRIX_FILE, delimiter=",", dtype=int)

    # initialize variables
    size = len(matrix)
    min_path_sum = math.inf
    min_matrix = np.zeros((size, size), dtype=int)

    # Dynamic Programming
    # We can move only up, down and right
    # We don't have to check left move
    for i in range(size):
        min_matrix[i][0] = matrix[i][0]

    for j in range(1, size):
        for i in range(size):
            min_matrix[i][j] = min_matrix[i][j - 1] + matrix[i][j]
        for i in range(1, size):
            min_matrix[i][j] = min(
                min_matrix[i][j], min_matrix[i - 1][j] + matrix[i][j]
            )
        for i in range(size - 2, -1, -1):
            min_matrix[i][j] = min(
                min_matrix[i][j], min_matrix[i + 1][j] + matrix[i][j]
            )
  
    # find minimum path sum
    for i in range(size):
        min_path_sum = min(min_path_sum, min_matrix[i][size - 1])

    return min_path_sum


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"--- {time.time() - start_time} seconds ---")

"""
--- 0.015109062194824219 seconds ---
"""
