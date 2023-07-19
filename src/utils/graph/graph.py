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
