"""Module with grid utils"""
import numpy as np


def read_grid(file_path):
    """Read grid from file"""
    return np.loadtxt(file_path, delimiter=",", dtype=int)


def get_grid_size(grid):
    """Get grid size"""
    return len(grid)


def get_grid_min_path_sum(grid):
    """Get grid minimum path sum"""
    size = get_grid_size(grid)
    min_path_sum = np.inf
    min_matrix = np.zeros((size, size), dtype=int)

    # Dynamic Programming
    # We can move in four directions
    for i in range(size):
        min_matrix[i][0] = grid[i][0]

    for j in range(1, size):
        for i in range(size):
            min_matrix[i][j] = min_matrix[i][j - 1] + grid[i][j]
        for i in range(1, size):
            min_matrix[i][j] = min(
                min_matrix[i][j], min_matrix[i - 1][j] + grid[i][j]
            )
        for i in range(size - 2, -1, -1):
            min_matrix[i][j] = min(
                min_matrix[i][j], min_matrix[i + 1][j] + grid[i][j]
            )

    # find minimum path sum
    for i in range(size):
        min_path_sum = min(min_path_sum, min_matrix[i][size - 1])

    return min_path_sum