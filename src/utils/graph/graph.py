"""Module with graph implementation."""
from typing import Dict, List, Optional, Set, Tuple

import numpy as np


class Graph:
    """Graph implementation."""

    def __init__(self, vertices: List[int], edges: List[Tuple[int, int]]):
        """Initialize graph.

        Args:
            vertices: list of vertices.
            edges: list of edges.
        """
        self._vertices = vertices
        self._edges = edges
        self._adjacency_list = self._build_adjacency_list()

    @property
    def vertices(self) -> List[int]:
        """Return list of vertices."""
        return self._vertices

    @property
    def edges(self) -> List[Tuple[int, int]]:
        """Return list of edges."""
        return self._edges

    @property
    def adjacency_list(self) -> Dict[int, List[int]]:
        """Return adjacency list."""
        return self._adjacency_list

    def _build_adjacency_list(self) -> Dict[int, List[int]]:
        adjacency_list = {vertex: [] for vertex in self._vertices}
        for edge in self._edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        return adjacency_list

    def breadth_first_search(self, start: int) -> List[int]:
        """Breadth first search algorithm.

        Args:
            start: start vertex.

        Returns:
            list of visited vertices.
        """
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(self._adjacency_list[vertex])
        return visited

    def depth_first_search(self, start: int) -> List[int]:
        """Depth first search algorithm.

        Args:
            start: start vertex.

        Returns:
            list of visited vertices.
        """
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(self._adjacency_list[vertex])
        return visited

    def _topological_sort_util(
        self, vertex: int, visited: Set[int], stack: List[int]
    ):
        visited.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                self._topological_sort_util(
                    adjacent_vertex, visited, stack
                )
        stack.insert(0, vertex)

    def topological_sort(self) -> Optional[List[int]]:
        """Topological sort algorithm.

        Returns:
            list of sorted vertices.
        """
        visited = set()
        stack = []
        for vertex in self._vertices:
            if vertex not in visited:
                self._topological_sort_util(
                    vertex, visited, stack
                )
        return stack[::-1]
    
    def _is_cyclic_util(
        self, vertex: int, visited: Set[int], stack: Set[int]
    ) -> bool:
        visited.add(vertex)
        stack.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                if self._is_cyclic_util(
                    adjacent_vertex, visited, stack
                ):
                    return True
            elif adjacent_vertex in stack:
                return True
        stack.remove(vertex)
        return False
    
    def is_cyclic(self) -> bool:
        """Check if graph is cyclic.

        Returns:
            True if graph is cyclic, False otherwise.
        """
        visited = set()
        stack = set()
        for vertex in self._vertices:
            if vertex not in visited:
                if self._is_cyclic_util(
                    vertex, visited, stack
                ):
                    return True
        return False
