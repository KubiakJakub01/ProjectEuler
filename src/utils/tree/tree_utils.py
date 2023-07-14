"""Module with tree utilities"""
import typing
import functools
import collections

from .tree_node import TreeNode


def create_tree_node_list_from_list_of_values(values: typing.List[typing.Any]) -> typing.List[TreeNode]:
    """Create a list of tree nodes from a list of values

    Args:
        values (typing.List[typing.Any]): The list of values

    Returns:
        typing.List[TreeNode]: The list of tree nodes
    """
    if not values:
        return []
    tree_node_list = []
    for value in values:
        if value is None:
            tree_node_list.append(None)
        else:
            tree_node_list.append(TreeNode(value))
    return tree_node_list


def create_tree_from_list_of_values(values: typing.List[typing.Any]) -> TreeNode:
    """Create a tree from a list of values

    Args:
        values (typing.List[typing.Any]): The list of values

    Returns:
        TreeNode: The root of the tree
    """
    if not values:
        return None
    tree_node_list = create_tree_node_list_from_list_of_values(values)
    for i, tree_node in enumerate(tree_node_list):
        if tree_node is None:
            continue
        if 2 * i + 1 < len(tree_node_list):
            tree_node.left = tree_node_list[2 * i + 1]
        if 2 * i + 2 < len(tree_node_list):
            tree_node.right = tree_node_list[2 * i + 2]
    return tree_node_list[0]


def create_list_of_values_from_tree(root: TreeNode) -> typing.List[typing.Any]:
    """Create a list of values from a tree

    Args:
        root (TreeNode): The root of the tree

    Returns:
        typing.List[typing.Any]: The list of values
    """
    if not root:
        return []
    value_list = []
    queue = collections.deque([root])
    while queue:
        tree_node = queue.popleft()
        if tree_node:
            value_list.append(tree_node.val)
            queue.append(tree_node.left)
            queue.append(tree_node.right)
        else:
            value_list.append(None)
    while value_list[-1] is None:
        value_list.pop()
    return value_list
