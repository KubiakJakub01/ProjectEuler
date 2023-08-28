"""Utils for Naray Tree"""
from typing import List, Optional, Tuple

from src.utils.tree.node import Node


class NarayTree:

    def __init__(self, root: Node):
        self.root = root

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)

    def __eq__(self, other):
        return self.root == other.root

    def __hash__(self):
        return hash(self.root)

    def __iter__(self):
        return self.root.__iter__()

    def __next__(self):
        return self.root.__next__()

    def __len__(self):
        return self.root.__len__()

    def __getitem__(self, item):
        return self.root.__getitem__(item)

    def __setitem__(self, key, value):
        self.root.__setitem__(key, value)

    def __delitem__(self, key):
        self.root.__delitem__(key)

    def __contains__(self, item):
        return self.root.__contains__(item)

    def __reversed__(self):
        return self.root.__reversed__()

    def __add__(self, other):
        return self.root.__add__(other)

    def __mul__(self, other):
        return self.root.__mul__(other)

    def __rmul__(self, other):
        return self.root.__rmul__(other)

    def __iadd__(self, other):
        return self.root.__iadd__(other)

    def __imul__(self, other):
        return self.root.__imul__(other)

    def __contains__(self, item):
        return self.root.__contains__(item)

    def __reversed__(self):
        return self.root.__reversed__()

    def __add__(self, other):
        return self.root.__add__(other)

    def __mul__(self, other):
        return self.root.__mul__(other)

    def __rmul__(self, other):
        return self.root.__rmul__(other)

    def __iadd__(self, other):
        return self.root.__iadd__(other)

    def __imul__(self, other):
        return self.root.__imul__(other)

    def __contains__(self, item):
        return self.root.__contains__(item)

    def __reversed__(self):
        return self.root.__reversed__()

    def __add__(self, other):
        return self.root.__add__(other)

    def __mul__(self, other):
        return self

    def __rmul__(self, other):
        return self.root.__rmul__(other)
    
    def __iadd__(self, other):
        return self.root.__iadd__(other)
