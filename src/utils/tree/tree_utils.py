"""Module with tree utilities"""
import typing
import functools
import collections

from node.tree_node import TreeNode


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


def printTree(node: TreeNode, level=0):
    """Print the tree.
    Args:
        node (BinaryNode): The current node.
    Returns:
        str: A string representation of the tree.
    """
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        printTree(node.right, level + 1)


def print_tree(func):
    """Print the tree.
    Args:
        func (typing.Callable): The function to be decorated.
    Returns:
        typing.Callable: The decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            typing.Any: The result of the decorated function.
        """
        result = func(*args, **kwargs)
        printTree(result)
        return result
    return wrapper


def get_tree_height(root: TreeNode) -> int:
    """Get the height of the tree.

    Args:
        root (TreeNode): The root of the tree.

    Returns:
        int: The height of the tree.
    """
    if not root:
        return 0
    return max(get_tree_height(root.left), get_tree_height(root.right)) + 1


def get_tree_height_iterative(root: TreeNode) -> int:
    """Get the height of the tree iteratively.

    Args:
        root (TreeNode): The root of the tree.

    Returns:
        int: The height of the tree.
    """
    if not root:
        return 0
    height = 0
    queue = collections.deque([root])
    while queue:
        height += 1
        for _ in range(len(queue)):
            tree_node = queue.popleft()
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
    return height
