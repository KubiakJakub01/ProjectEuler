'''Utils for file I/O'''
import csv
import json
import logging
import sys
import tarfile
from pathlib import Path

import yaml


def read_file(path: Path):
    """Read file from given path

    Args:
        path: path to file

    Returns:
        list: list of lines
    """
    if not path.is_file():
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return p.read().splitlines()


def write_file(path: Path, content: str):
    """Write content to file

    Args:
        path: path to file
        content: content to write
    """
    with open(path, "w") as p:
        p.write(content)


def read_csv(path: Path, columns=None):
    """Read csv file from given path

    Args:
        path: path to file

    Returns:
        list: list of rows
    """
    if not path.is_file():
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        reader = csv.reader(p)
        header = next(reader)
        if columns:
            header = columns
        return [dict(zip(header, row)) for row in reader]


def write_csv(path: Path, content: list):
    """Write content to csv file

    Args:
        path: path to file
        content: content to write
    """
    with open(path, "w") as p:
        csv.writer(p).writerows(content)


def read_json(path: Path):
    """Read json file from given path

    Args:
        path: path to file

    Returns:
        dict: json object
    """
    if not path.is_file():
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return json.load(p)


def write_json(path: Path, content: dict):
    """Write content to json file

    Args:
        path: path to file
        content: content to write
    """
    with open(path, "w") as p:
        json.dump(content, p, indent=4)


def read_yaml(path: Path):
    """Read yaml file from given path

    Args:
        path: path to file

    Returns:
        dict: yaml object
    """
    if not path.is_file():
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return yaml.safe_load(p)


def write_yaml(path: Path, content: dict):
    """Write content to yaml file

    Args:
        path: path to file
        content: content to write
    """
    with open(path, "w") as p:
        yaml.dump(content, p, default_flow_style=False)


def read_file_by_line(path: Path):
    """Read file from given path

    Args:
        path: path to file

    Returns:
        list: list of lines
    """
    if not path.is_file():
        logging.error("File does not exist")
        sys.exit(1)

    with open(path) as p:
        return p.readlines()


def tar_files(tar_name: str, files: list):
    """Tar files

    Args:
        tar_name: name of tar file
        files: list of files to tar
    """
    with tarfile.open(tar_name, "w:gz") as tar:
        for file in files:
            tar.add(file)

