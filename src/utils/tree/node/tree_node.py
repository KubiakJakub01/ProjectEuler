"""Module with tree node class"""
import typing


class TreeNode:
    """Class representing a tree node"""

    def __init__(
        self,
        value: typing.Any,
        left: typing.Optional["TreeNode"] = None,
        right: typing.Optional["TreeNode"] = None,
    ):
        """Initialize a tree node

        Args:
            val (typing.Any): The value of the node
            left (typing.Optional["TreeNode"], optional): The left child of the node. Defaults to None.
            right (typing.Optional["TreeNode"], optional): The right child of the node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation of the tree node

        Returns:
            str: The string representation of the tree node
        """
        return f"TreeNode({self.value}, {self.left}, {self.right})"

    def __str__(self) -> str:
        """Return a string representation of the tree node

        Returns:
            str: The string representation of the tree node
        """
        return f"TreeNode({self.value}, {self.left}, {self.right})"


class BinaryNode(TreeNode):
    """Class representing a binary tree node"""

    def __init__(
        self,
        value: typing.Any,
        left: typing.Optional["BinaryNode"] = None,
        right: typing.Optional["BinaryNode"] = None,
    ):
        """Initialize a binary tree node

        Args:
            val (typing.Any): The value of the node
            left (typing.Optional["BinaryNode"], optional): The left child of the node. Defaults to None.
            right (typing.Optional["BinaryNode"], optional): The right child of the node. Defaults to None.
        """
        super().__init__(value, left, right)

    def __repr__(self) -> str:
        """Return a string representation of the binary tree node

        Returns:
            str: The string representation of the binary tree node
        """
        return f"BinaryNode({self.value}, {self.left}, {self.right})"

    def __str__(self) -> str:
        """Return a string representation of the binary tree node

        Returns:
            str: The string representation of the binary tree node
        """
        return f"BinaryNode({self.value}, {self.left}, {self.right})"
