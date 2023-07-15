"""Module with binary tree implementation."""
import collections
from typing import Any, Optional, Tuple

from node.tree_node import BinaryNode
from tree_utils import printTree
from tree import Tree


class BinaryTree(Tree):
    """A binary tree implementation."""

    def __init__(self, root: Optional[BinaryNode] = None) -> None:
        """Initialize a binary tree.

        Args:
            root (Optional[BinaryNode], optional): The root node of the tree. Defaults to None.
        """
        self.root = root

    def __repr__(self) -> str:
        """Return a string representation of the tree.

        Returns:
            str: A string representation of the tree.
        """
        return f"BinaryTree(root={self.root})"

    def __str__(self) -> str:
        """Return a string representation of the tree.

        Returns:
            str: A string representation of the tree.
        """
        return f"BinaryTree(root={self.root})"

    def __eq__(self, other: Any) -> bool:
        """Return whether two trees are equal.

        Args:
            other (Any): The other tree to compare to.

        Returns:
            bool: Whether the two trees are equal.
        """
        if not isinstance(other, BinaryTree):
            return False
        return self.root == other.root

    def __ne__(self, other: Any) -> bool:
        """Return whether two trees are not equal.

        Args:
            other (Any): The other tree to compare to.

        Returns:
            bool: Whether the two trees are not equal.
        """
        return not self.__eq__(other)

    def __bool__(self) -> bool:
        """Return whether the tree is not empty.

        Returns:
            bool: Whether the tree is not empty.
        """
        return bool(self.root)

    def __len__(self) -> int:
        """Return the number of nodes in the tree.

        Returns:
            int: The number of nodes in the tree.
        """
        return self.size()

    def __contains__(self, item: Any) -> bool:
        """Return whether the tree contains a node with the given value.

        Args:
            item (Any): The value to search for.

        Returns:
            bool: Whether the tree contains a node with the given value.
        """
        return self.contains(item)
    
    def size(self) -> int:
        """Return the number of nodes in the tree.

        Returns:
            int: The number of nodes in the tree.
        """
        return self._size(self.root)

    def _size(self, node: Optional[BinaryNode] = None, count: int = 0) -> int:
        """Return the number of nodes in the tree.

        Args:
            node (Optional): The current node.
            count (int, optional): The current count. Defaults to 0.

        Returns:
            int: The number of nodes in the tree.
        """
        if node is None:
            return count
        count += 1
        count = self._size(node.left, count)
        count = self._size(node.right, count)
        return count
    
    def add(self, item: Any) -> None:
        """Add a node with the given value to the tree.

        Args:
            item (Any): The value of the node to add.
        """
        if self.root is None:
            self.root = BinaryNode(item)
        else:
            self._add(item, self.root)

    def _add(self, item: Any, node: BinaryNode) -> None:
        """Add a node with the given value to the tree.

        Args:
            item (Any): The value of the node to add.
            node (BinaryNode): The current node.
        """
        if item < node.value:
            if node.left is None:
                node.left = BinaryNode(item)
            else:
                self._add(item, node.left)
        else:
            if node.right is None:
                node.right = BinaryNode(item)
            else:
                self._add(item, node.right)

    def remove(self, item: Any) -> None:
        """Remove a node with the given value from the tree.

        Args:
            item (Any): The value of the node to remove.
        """
        self.root = self._remove(item, self.root)

    def _remove(self, item: Any, node: BinaryNode) -> Optional[BinaryNode]:
        """Remove a node with the given value from the tree.

        Args:
            item (Any): The value of the node to remove.
            node (BinaryNode): The current node.

        Returns:
            Optional[BinaryNode]: The new root node of the tree.
        """
        if node is None:
            return None
        if item < node.value:
            node.left = self._remove(item, node.left)
            return node
        if item > node.value:
            node.right = self._remove(item, node.right)
            return node
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        temp = self._find_min(node.right)
        node.value = temp.value
        node.right = self._remove(temp.value, node.right)

    def _find_min(self, node: BinaryNode) -> BinaryNode:
        """Return the minimum node in the tree.

        Args:
            node (BinaryNode): The current node.

        Returns:
            BinaryNode: The minimum node in the tree.
        """
        while node.left is not None:
            node = node.left
        return node
    
    def contains(self, item: Any) -> bool:
        """Return whether the tree contains a node with the given value.

        Args:
            item (Any): The value to search for.

        Returns:
            bool: Whether the tree contains a node with the given value.
        """
        return self._contains(self.root, item)
    
    def _contains(self, node: Optional[BinaryNode], item: Any) -> bool:
        """Return whether the tree contains a node with the given value.

        Args:
            node (Optional): The current node.
            item (Any): The value to search for.

        Returns:
            bool: Whether the tree contains a node with the given value.
        """
        if node is None:
            return False
        if node.value == item:
            return True
        return self._contains(node.left, item) or self._contains(node.right, item)
    
    def height(self) -> int:
        """Return the height of the tree.

        Returns:
            int: The height of the tree.
        """
        return self._height(self.root)
    
    def _height(self, node: Optional[BinaryNode]= None) -> int:
        """Return the height of the tree.

        Args:
            node (Optional): The current node.

        Returns:
            int: The height of the tree.
        """
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def is_balanced(self) -> bool:
        """Return whether the tree is balanced.

        Returns:
            bool: Whether the tree is balanced.
        """
        return self._is_balanced(self.root)
    
    def _is_balanced(self, node: Optional[BinaryNode] = None) -> bool:
        """Return whether the tree is balanced.

        Args:
            node (Optional): The current node.

        Returns:
            bool: Whether the tree is balanced.
        """
        if node is None:
            return True
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)
    
    def is_full(self) -> bool:
        """Return whether the tree is full.

        Returns:
            bool: Whether the tree is full.
        """
        return self._is_full(self.root)
    
    def _is_full(self, node: Optional[BinaryNode] = None) -> bool:
        """Return whether the tree is full.

        Args:
            node (Optional): The current node.

        Returns:
            bool: Whether the tree is full.
        """
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_full(node.left) and self._is_full(node.right)
        return False
    
    def is_perfect(self) -> bool:
        """Return whether the tree is perfect.

        Returns:
            bool: Whether the tree is perfect.
        """
        return self._is_perfect(self.root)
    
    def _is_perfect(self, node: Optional[BinaryNode]= None) -> bool:
        """Return whether the tree is perfect.

        Args:
            node (Optional): The current node.

        Returns:
            bool: Whether the tree is perfect.
        """
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_perfect(node.left) and self._is_perfect(node.right)
        return False

    def is_complete(self) -> bool:
        """Return whether the tree is complete.

        Returns:
            bool: Whether the tree is complete.
        """
        return self._is_complete(self.root)
    
    def _is_complete(self, node: Optional[BinaryNode] = None) -> bool:
        """Return whether the tree is complete.

        Args:
            node (Optional): The current node.

        Returns:
            bool: Whether the tree is complete.
        """
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self._is_complete(node.left) and self._is_complete(node.right)
        if node.left is not None and node.right is None:
            return False
        if node.left is None and node.right is not None:
            return False
        return False

    def is_degenerate(self) -> bool:
        """Return whether the tree is degenerate.

        Returns:
            bool: Whether the tree is degenerate.
        """
        return self._is_degenerate(self.root)
    
    def _is_degenerate(self, node: Optional[BinaryNode] = None) -> bool:
        """Return whether the tree is degenerate.

        Args:
            node (Optional): The current node.

        Returns:
            bool: Whether the tree is degenerate.
        """
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return False
        return self._is_degenerate(node.left) or self._is_degenerate(node.right)


if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()

    # Add nodes to the tree
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)

    # Print the tree
    print(tree)

    # Print the size of the tree
    print(f"Size: {tree.size()}")

    # Print whether the tree contains a node with the given value
    print(f"Contains 5: {tree.contains(5)}")

    # Print the height of the tree
    print(f"Height: {tree.height()}")

    # Plot the tree
    printTree(tree.root)
