"""Module with segment tree utils"""
import math

import numpy as np

from node.tree_node import TreeNode

class SegmentTree:
    """Segment tree class"""
    def __init__(self, array):
        self.array = array
        self.root = self.build_tree(0, len(array) - 1)

    def build_tree(self, start, end):
        """Build tree"""
        if start == end:
            return TreeNode(self.array[start], start, end)
        mid = (start + end) // 2
        left = self.build_tree(start, mid)
        right = self.build_tree(mid + 1, end)
        return TreeNode(left.value + right.value, start, end, left, right)

    def update(self, index, value):
        """Update value"""
        self.update_tree(self.root, index, value)

    def update_tree(self, root, index, value):
        """Update tree"""
        if root.start == root.end:
            root.value = value
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.update_tree(root.left, index, value)
        else:
            self.update_tree(root.right, index, value)
        root.value = root.left.value + root.right.value

    def query(self, start, end):
        """Query"""
        return self.query_tree(self.root, start, end)

    def query_tree(self, root, start, end):
        """Query tree"""
        if root.start == start and root.end == end:
            return root.value
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.query_tree(root.left, start, end)
        if start > mid:
            return self.query_tree(root.right, start, end)
        return (
            self.query_tree(root.left, start, mid)
            + self.query_tree(root.right, mid + 1, end)
        )

    def __repr__(self):
        return f"SegmentTree({self.array})"

    def __str__(self):
        return f"SegmentTree({self.array})"

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.update(index, value)

    def __iter__(self):
        return iter(self.array)

    def __reversed__(self):
        return reversed(self.array)

    def __contains__(self, item):
        return
