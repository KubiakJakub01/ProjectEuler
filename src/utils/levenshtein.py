"""Script with the Levenshtein distance algorithm."""
import numpy as np
from levenshtein import levenshtein


def levenshtein_distance(string_1: str, string_2: str):
    """Return the Levenshtein distance between two strings.

    Args:
        string_1: The first string
        string_2: The second string

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


def levenshtein_distance_matrix(strings: list[str]):
    """Return the Levenshtein distance matrix between a list of strings.

    Args:
        strings: A list of strings

    Returns:
        np.array: The Levenshtein distance matrix
    """
    matrix = np.zeros((len(strings), len(strings)))
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            matrix[i, j] = levenshtein_distance(strings[i], strings[j])
            matrix[j, i] = matrix[i, j]
    return matrix


def levenshtein_distance_matrix_fast(strings: list[str]):
    """Return the Levenshtein distance matrix between a list of strings.

    Args:
        strings: A list of strings

    Returns:
        np.array: The Levenshtein distance matrix
    """
    matrix = np.zeros((len(strings), len(strings)))
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            matrix[i, j] = levenshtein(strings[i], strings[j])
            matrix[j, i] = matrix[i, j]
    return matrix


def remove_duplicates(strings: list[str]):
    """Return a list of strings without duplicates.

    Args:
        strings: A list of strings

    Returns:
        list: A list of strings without duplicates
    """
    strings = list(set(strings))
    strings.sort()
    return strings


def remove_punctuation(string: str):
    """Return a string without punctuation.

    Args:
        string: A string

    Returns:
        str: The string without punctuation
    """
    punctuation = [".", ",", ":", ";", "!", "?", '"', "'"]
    for char in punctuation:
        string = string.replace(char, "")
    return string


def normalize(string: str):
    """Return a string without punctuation and in lowercase.

    Args:
        string: A string

    Returns:
        str: The string without punctuation and in lowercase
    """
    return remove_punctuation(string).lower()


def normalize_list(strings: list[str]):
    """Return a list of strings without punctuation and in lowercase.

    Args:
        strings: A list of strings

    Returns:
        list: A list of strings without punctuation and in lowercase
    """
    return [normalize(string) for string in strings]


def remove_stopwords(string: str, stopwords: list[str]):
    """Return a string without stopwords.

    Args:
        string: A string
        stopwords: A list of stopwords

    Returns:
        str: The string without stopwords
    """
    return " ".join([word for word in string.split() if word not in stopwords])


def remove_stopwords_list(strings: list[str], stopwords: list[str]):
    """Return a list of strings without stopwords.

    Args:
        strings: A list of strings
        stopwords: A list of stopwords

    Returns:
        list: A list of strings without stopwords
    """
    return [remove_stopwords(string, stopwords) for string in strings]


def remove_duplicates_and_stopwords(strings: list[str], stopwords: list[str]):
    """Return a list of strings without duplicates and stopwords.

    Args:
        strings: A list of strings
        stopwords: A list of stopwords

    Returns:
        list: A list of strings without duplicates and stopwords
    """
    strings = remove_duplicates(strings)
    strings = remove_stopwords_list(strings, stopwords)
    return strings


def levenshtein_distance_matrix_normalized(strings: list[str], stopwords: list[str]):
    """Return the Levenshtein distance matrix between a list of strings.

    Args:
        strings: A list of strings
        stopwords: A list of stopwords

    Returns:
        np.array: The Levenshtein distance matrix
    """
    strings = remove_duplicates_and_stopwords(strings, stopwords)
    strings = normalize_list(strings)
    return levenshtein_distance_matrix(strings)


def levenshtein_distance_matrix_normalized_fast(
    strings: list[str], stopwords: list[str]
):
    """Return the Levenshtein distance matrix between a list of strings.

    Args:
        strings: A list of strings
        stopwords: A list of stopwords

    Returns:
        np.array: The Levenshtein distance matrix
    """
    strings = remove_duplicates_and_stopwords(strings, stopwords)
    strings = normalize_list(strings)
    return levenshtein_distance_matrix_fast(strings)
