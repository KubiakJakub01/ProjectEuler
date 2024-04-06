"""Utils for file I/O"""
import csv
import json
import logging
import sys
import tarfile
import zipfile
from pathlib import Path

import yaml
from pypdf import PdfReader


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


def untar_files(tar_name: str, dest: str):
    """Untar files

    Args:
        tar_name: name of tar file
        dest: destination to untar
    """
    with tarfile.open(tar_name, "r:gz") as tar:
        tar.extractall(path=dest)


def zip_files_and_directories(source_path, target_zip_path):
    source_path = Path(source_path)
    target_zip_path = Path(target_zip_path)

    with zipfile.ZipFile(target_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        if source_path.is_dir():
            for file in source_path.rglob("*"):
                zipf.write(file, file.relative_to(source_path.parent))
        else:
            zipf.write(source_path, source_path.name)


def unzip_files(zip_path, target_dir):
    zip_path = Path(zip_path)
    target_dir = Path(target_dir)

    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(target_dir)


def read_pdf(path: Path):
    """Read pdf file from given path

    Args:
        path: path to file

    Returns:
        list: list of pages
    """
    if not path.is_file():
        logging.error("File does not exist")
        sys.exit(1)

    reader = PdfReader(path)
    return [page.extract_text() for page in reader.pages]


def write_pdf(path: Path, content: list):
    """Write content to pdf file

    Args:
        path: path to file
        content: content to write
    """
    with open(path, "w") as p:
        p.write(content)
