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
            min_matrix[i][j] = min(min_matrix[i][j], min_matrix[i - 1][j] + grid[i][j])
        for i in range(size - 2, -1, -1):
            min_matrix[i][j] = min(min_matrix[i][j], min_matrix[i + 1][j] + grid[i][j])

    # find minimum path sum
    for i in range(size):
        min_path_sum = min(min_path_sum, min_matrix[i][size - 1])

    return min_path_sum


def get_grid_max_path(grid):
    """Get grid maximum path"""
    size = get_grid_size(grid)
    max_path = np.zeros(size, dtype=int)
    max_path[0] = 0

    for j in range(1, size):
        for i in range(size):
            max_path[i] = max(max_path[i], grid[i][j - 1])

        for i in range(size):
            if i == 0:
                grid[i][j] += max(max_path[i], max_path[i + 1])
            elif i == size - 1:
                grid[i][j] += max(max_path[i], max_path[i - 1])
            else:
                grid[i][j] += max(max_path[i], max(max_path[i - 1], max_path[i + 1]))

    max_path_sum = 0
    for i in range(size):
        max_path_sum = max(max_path_sum, grid[i][size - 1])

    return max_path_sum


def get_grid_max_path_sum(grid):
    """Get grid maximum path sum"""
    size = get_grid_size(grid)
    max_path_sum = np.zeros((size, size), dtype=int)

    for i in range(size):
        max_path_sum[i][0] = grid[i][0]

    for j in range(1, size):
        for i in range(size):
            max_path_sum[i][j] = grid[i][j] + max(max_path_sum[i][j - 1], max_path_sum[i][j])

        for i in range(1, size):
            max_path_sum[i][j] = max(max_path_sum[i][j], max_path_sum[i - 1][j] + grid[i][j])

        for i in range(size - 2, -1, -1):
            max_path_sum[i][j] = max(max_path_sum[i][j], max_path_sum[i + 1][j] + grid[i][j])

    max_path_sum_result = 0
    for i in range(size):
        max_path_sum_result = max(max_path_sum_result, max_path_sum[i][size - 1])

    return max_path_sum_result
