'''Script with the Levenshtein distance algorithm.'''
import numpy as np


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
