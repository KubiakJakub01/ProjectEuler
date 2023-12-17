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
