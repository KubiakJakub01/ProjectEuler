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

