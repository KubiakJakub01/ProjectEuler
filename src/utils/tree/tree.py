"""Class with base tree classes"""
from typing import Any, Optional
from abc import ABC, abstractmethod

from node.tree_node import TreeNode


class Tree(ABC):
    """Class representing a tree"""

    def __init__(self, root: Optional[TreeNode] = None):
        """Initialize a tree

        Args:
            root (typing.Optional[TreeNode], optional): The root of the tree. Defaults to None.
        """
        self.root = root

    @abstractmethod
    def __repr__(self) -> str:
        """Return a string representation of the tree

        Returns:
            str: The string representation of the tree
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the tree

        Returns:
            str: The string representation of the tree
        """
        pass

    @abstractmethod
    def __eq__(self, o: object) -> bool:
        """Check if two trees are equal

        Args:
            o (object): The other tree

        Returns:
            bool: True if the two trees are equal, False otherwise
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the length of the tree

        Returns:
            int: The length of the tree
        """
        pass

    @abstractmethod
    def __contains__(self, value: Any) -> bool:
        """Check if the tree contains a value

        Args:
            value (typing.Any): The value to check

        Returns:
            bool: True if the tree contains the value, False otherwise
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """Return the size of the tree

        Returns:
            int: The size of the tree
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the tree is empty

        Returns:
            bool: True if the tree is empty, False otherwise
        """
        pass

    @abstractmethod
    def height(self) -> int:
        """Return the height of the tree

        Returns:
            int: The height of the tree
        """
        pass

    @abstractmethod
    def add(self, value: Any) -> None:
        """Add a value to the tree

        Args:
            value (Any): The value to add
        """
        pass

    @abstractmethod
    def remove(self, value: Any) -> None:
        """Remove a value from the tree

        Args:
            value (Any): The value to remove
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear the tree"""
        pass
