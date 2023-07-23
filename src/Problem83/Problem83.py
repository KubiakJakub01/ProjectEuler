"""
Created on 23.07.2023 12:35

Problem 83: Path Sum: Four Ways
https://projecteuler.net/problem=83

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
    # We have to find minimum path sum from top left corner to bottom right corner
    # We can move in all four directions
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

    for j in range(size - 2, -1, -1):
        for i in range(size):
            min_matrix[i][j] = min(min_matrix[i][j], min_matrix[i][j + 1])
        for i in range(1, size):
            min_matrix[i][j] = min(
                min_matrix[i][j], min_matrix[i - 1][j] + matrix[i][j]
            )
        for i in range(size - 2, -1, -1):
            min_matrix[i][j] = min(
                min_matrix[i][j], min_matrix[i + 1][j] + matrix[i][j]
            )

    # find minimum path sum
    min_path_sum = min_matrix[size - 1][size - 1]

    return min_path_sum


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print(f"--- {time.time() - start_time} seconds ---")
