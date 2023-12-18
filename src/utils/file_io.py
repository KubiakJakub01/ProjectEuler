'''Utils for file I/O'''
import os
import sys
import logging


def read_file(path):
    """Read file from given path

    Args:
        path (str): path to file

    Returns:
        list: list of lines
    """
    if not os.path.isfile(path):
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return p.read().splitlines()


def write_file(path, content):
    """Write content to file

    Args:
        path (str): path to file
        content (str): content to write
    """
    with open(path, "w") as p:
        p.write(content)
