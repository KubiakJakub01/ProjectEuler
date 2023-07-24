"""Module with grid utils"""
import numpy as np


def read_grid(file_path):
    """Read grid from file"""
    return np.loadtxt(file_path, delimiter=",", dtype=int)
