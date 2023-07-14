"""Module with tree node class"""
import typing


class TreeNode:
    """Class representing a tree node"""

    def __init__(self, val: typing.Any, left: typing.Optional["TreeNode"] = None,
                 right: typing.Optional["TreeNode"] = None):
        """Initialize a tree node

        Args:
            val (typing.Any): The value of the node
            left (typing.Optional["TreeNode"], optional): The left child of the node. Defaults to None.
            right (typing.Optional["TreeNode"], optional): The right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation of the tree node

        Returns:
            str: The string representation of the tree node
        """
        return f"TreeNode({self.val}, {self.left}, {self.right})"

    def __str__(self) -> str:
        """Return a string representation of the tree node

        Returns:
            str: The string representation of the tree node
        """
        return f"TreeNode({self.val}, {self.left}, {self.right})"
