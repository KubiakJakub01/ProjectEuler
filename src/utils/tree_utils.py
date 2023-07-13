"""Module with tree utilities"""
import collections
import typing

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
