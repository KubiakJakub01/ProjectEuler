"""Module with network implementation."""
from typing import Dict, List, Optional, Set, Tuple

import numpy as np


class Network:
    """Network implementation."""

    def __init__(self, vertices: List[int], edges: List[Tuple[int, int]]):
        """Initialize network.

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

    def _get_connected_components(self) -> List[Set[int]]:
        visited = set()
        connected_components = []
        for vertex in self._vertices:
            if vertex not in visited:
                connected_component = self.depth_first_search(vertex)
                connected_components.append(connected_component)
                visited.update(connected_component)
        return connected_components

    def _get_connected_components_with_vertex(self, vertex: int) -> List[Set[int]]:
        visited = set()
        connected_components = []
        for connected_component in self._get_connected_components():
            if vertex in connected_component:
                connected_components.append(connected_component)
                visited.update(connected_component)
        return connected_components

    def _get_connected_components_without_vertex(self, vertex: int) -> List[Set[int]]:
        visited = set()
        connected_components = []
        for connected_component in self._get_connected_components():
            if vertex not in connected_component:
                connected_components.append(connected_component)
                visited.update(connected_component)
        return connected_components

    def _get_connected_components_with_edge(self, edge: Tuple[int, int]) -> List[Set[int]]:
        visited = set()
        connected_components = []
        for connected_component in self._get_connected_components():
            if edge[0] in connected_component and edge[1] in connected_component:
                connected_components.append(connected_component)
                visited.update(connected_component)
        return connected_components
