'''Script with the Levenshtein distance algorithm.'''
import numpy as np
from levenshtein import levenshtein


def levenshtein_distance(string_1, string_2):
    """Return the Levenshtein distance between two strings.

    Args:
        string_1 (str): The first string
        string_2 (str): The second string

    Returns:
        int: The Levenshtein distance between the two strings
    """
    if len(string_1) > len(string_2):
        string_1, string_2 = string_2, string_1
    distances = range(len(string_1) + 1)
    for index_2, char_2 in enumerate(string_2):
        new_distances = [index_2 + 1]
        for index_1, char_1 in enumerate(string_1):
            if char_1 == char_2:
                new_distances.append(distances[index_1])
            else:
                new_distances.append(
                    1
                    + min(
                        (
                            distances[index_1],
                            distances[index_1 + 1],
                            new_distances[-1],
                        )
                    )
                )
        distances = new_distances
    return distances[-1]


def levenshtein_distance_matrix(strings):
    """Return the Levenshtein distance matrix between a list of strings.

    Args:
        strings (list): A list of strings

    Returns:
        np.array: The Levenshtein distance matrix
    """
    matrix = np.zeros((len(strings), len(strings)))
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            matrix[i, j] = levenshtein_distance(strings[i], strings[j])
            matrix[j, i] = matrix[i, j]
    return matrix


def levenshtein_distance_matrix_fast(strings):
    """Return the Levenshtein distance matrix between a list of strings.

    Args:
        strings (list): A list of strings

    Returns:
        np.array: The Levenshtein distance matrix
    """
    matrix = np.zeros((len(strings), len(strings)))
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            matrix[i, j] = levenshtein(strings[i], strings[j])
            matrix[j, i] = matrix[i, j]
    return matrix


def remove_duplicates(strings):
    """Return a list of strings without duplicates.

    Args:
        strings (list): A list of strings

    Returns:
        list: A list of strings without duplicates
    """
    strings = list(set(strings))
    strings.sort()
    return strings
