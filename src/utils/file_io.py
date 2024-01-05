'''Utils for file I/O'''
import csv
import json
import logging
import os
import sys

import yaml


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


def read_csv(path, columns=None):
    """Read csv file from given path

    Args:
        path (str): path to file

    Returns:
        list: list of rows
    """
    if not os.path.isfile(path):
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        reader = csv.reader(p)
        header = next(reader)
        if columns:
            header = columns
        return [dict(zip(header, row)) for row in reader]


def write_csv(path, content):
    """Write content to csv file

    Args:
        path (str): path to file
        content (list): content to write
    """
    with open(path, "w") as p:
        csv.writer(p).writerows(content)


def read_json(path):
    """Read json file from given path

    Args:
        path (str): path to file

    Returns:
        dict: json object
    """
    if not os.path.isfile(path):
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return json.load(p)


def write_json(path, content):
    """Write content to json file

    Args:
        path (str): path to file
        content (dict): content to write
    """
    with open(path, "w") as p:
        json.dump(content, p, indent=4)


def read_yaml(path):
    """Read yaml file from given path

    Args:
        path (str): path to file

    Returns:
        dict: yaml object
    """
    if not os.path.isfile(path):
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return yaml.safe_load(p)


def write_yaml(path, content):
    """Write content to yaml file

    Args:
        path (str): path to file
        content (dict): content to write
    """
    with open(path, "w") as p:
        yaml.dump(content, p, default_flow_style=False)


def read_file_by_line(path):
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
        return p.readlines()
