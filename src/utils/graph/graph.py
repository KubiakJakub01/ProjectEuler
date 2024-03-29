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

    def _topological_sort_util(self, vertex: int, visited: Set[int], stack: List[int]):
        visited.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                self._topological_sort_util(adjacent_vertex, visited, stack)
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
                self._topological_sort_util(vertex, visited, stack)
        return stack[::-1]

    def _is_cyclic_util(self, vertex: int, visited: Set[int], stack: Set[int]) -> bool:
        visited.add(vertex)
        stack.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                if self._is_cyclic_util(adjacent_vertex, visited, stack):
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
                if self._is_cyclic_util(vertex, visited, stack):
                    return True
        return False

    def _is_bipartite_util(self, vertex: int, color: Dict[int, int]) -> bool:
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in color:
                color[adjacent_vertex] = 1 - color[vertex]
                if not self._is_bipartite_util(adjacent_vertex, color):
                    return False
            elif color[adjacent_vertex] == color[vertex]:
                return False
        return True

    def is_bipartite(self) -> bool:
        """Check if graph is bipartite.

        Returns:
            True if graph is bipartite, False otherwise.
        """
        color = {self._vertices[0]: 0}
        return self._is_bipartite_util(self._vertices[0], color)

    def dijkstra(self, start: int, end: int) -> List[int]:
        """Dijkstra algorithm.

        Args:
            start: start vertex.
            end: end vertex.

        Returns:
            list with shortest path.
        """
        distance = {vertex: np.inf for vertex in self._vertices}
        parent = {vertex: None for vertex in self._vertices}
        distance[start] = 0
        queue = self._vertices.copy()
        while queue:
            vertex = min(queue, key=lambda vertex: distance[vertex])
            queue.remove(vertex)
            for adjacent_vertex in self._adjacency_list[vertex]:
                if adjacent_vertex in queue:
                    new_distance = distance[vertex] + 1
                    if new_distance < distance[adjacent_vertex]:
                        distance[adjacent_vertex] = new_distance
                        parent[adjacent_vertex] = vertex
        path = []
        vertex = end
        while vertex is not None:
            path.append(vertex)
            vertex = parent[vertex]
        return path[::-1]

    def bellman_ford(self, start: int) -> Tuple[Dict[int, int], Dict[int, int]]:
        """Bellman-Ford algorithm.

        Args:
            start: start vertex.

        Returns:
            tuple with distance and parent dictionaries.
        """
        distance = {vertex: np.inf for vertex in self._vertices}
        parent = {vertex: None for vertex in self._vertices}
        distance[start] = 0
        for _ in range(len(self._vertices) - 1):
            for edge in self._edges:
                if distance[edge[0]] + 1 < distance[edge[1]]:
                    distance[edge[1]] = distance[edge[0]] + 1
                    parent[edge[1]] = edge[0]
        return distance, parent

    def _get_adjacency_list(
        self, vertices: List[int], edges: List[Tuple[int, int]]
    ) -> Dict[int, List[int]]:
        adjacency_list = {vertex: [] for vertex in vertices}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
        return adjacency_list

    def _get_edges(
        self, vertices: List[int], edges: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return [(edge[0], edge[1]) for edge in edges]

    def __repr__(self) -> str:
        return str(self._adjacency_list)

    def __str__(self) -> str:
        return str(self._adjacency_list)


class DirectedGraph(Graph):
    """Directed graph implementation."""

    def __init__(self, vertices: List[int], edges: List[Tuple[int, int]]):
        """Initialize directed graph.

        Args:
            vertices: list of vertices.
            edges: list of edges.
        """
        super().__init__(vertices, edges)
        self._adjacency_list = self._get_adjacency_list(vertices, edges)
        self._edges = self._get_edges(vertices, edges)

    def _get_adjacency_list(
        self, vertices: List[int], edges: List[Tuple[int, int]]
    ) -> Dict[int, List[int]]:
        adjacency_list = {vertex: [] for vertex in vertices}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
        return adjacency_list

    def _get_edges(
        self, vertices: List[int], edges: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        return edges

    def _topological_sort_util(self, vertex: int, visited: Set[int], stack: List[int]):
        visited.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                self._topological_sort_util(adjacent_vertex, visited, stack)
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
                self._topological_sort_util(vertex, visited, stack)
        return stack[::-1]

    def _is_cyclic_util(self, vertex: int, visited: Set[int], stack: Set[int]) -> bool:
        visited.add(vertex)
        stack.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                if self._is_cyclic_util(adjacent_vertex, visited, stack):
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
                if self._is_cyclic_util(vertex, visited, stack):
                    return True
        return False


class WeightedGraph(Graph):
    """Weighted graph implementation."""

    def __init__(self, vertices: List[int], edges: List[Tuple[int, int, int]]):
        """Initialize weighted graph.

        Args:
            vertices: list of vertices.
            edges: list of edges.
        """
        super().__init__(vertices, edges)
        self._adjacency_list = self._get_adjacency_list(vertices, edges)
        self._edges = self._get_edges(vertices, edges)

    def _get_adjacency_list(
        self, vertices: List[int], edges: List[Tuple[int, int, int]]
    ) -> Dict[int, List[int]]:
        adjacency_list = {vertex: [] for vertex in vertices}
        for edge in edges:
            adjacency_list[edge[0]].append((edge[1], edge[2]))
            adjacency_list[edge[1]].append((edge[0], edge[2]))
        return adjacency_list

    def _get_edges(
        self, vertices: List[int], edges: List[Tuple[int, int, int]]
    ) -> List[Tuple[int, int]]:
        return [(edge[0], edge[1]) for edge in edges]

    def dijkstra(self, start: int) -> Tuple[Dict[int, int], Dict[int, int]]:
        """Dijkstra algorithm.

        Args:
            start: start vertex.

        Returns:
            tuple with distance and parent dictionaries.
        """
        distance = {vertex: np.inf for vertex in self._vertices}
        parent = {vertex: None for vertex in self._vertices}
        distance[start] = 0
        queue = self._vertices.copy()
        while queue:
            vertex = min(queue, key=lambda vertex: distance[vertex])
            queue.remove(vertex)
            for adjacent_vertex, weight in self._adjacency_list[vertex]:
                if adjacent_vertex in queue:
                    new_distance = distance[vertex] + weight
                    if new_distance < distance[adjacent_vertex]:
                        distance[adjacent_vertex] = new_distance
                        parent[adjacent_vertex] = vertex
        return distance, parent

    def bellman_ford(self, start: int) -> Tuple[Dict[int, int], Dict[int, int]]:
        """Bellman-Ford algorithm.

        Args:
            start: start vertex.

        Returns:
            tuple with distance and parent dictionaries.
        """
        distance = {vertex: np.inf for vertex in self._vertices}
        parent = {vertex: None for vertex in self._vertices}
        distance[start] = 0
        for _ in range(len(self._vertices) - 1):
            for edge in self._edges:
                if distance[edge[0]] + 1 < distance[edge[1]]:
                    distance[edge[1]] = distance[edge[0]] + 1
                    parent[edge[1]] = edge[0]
        return distance, parent


class DirectedWeightedGraph(WeightedGraph):
    """Directed weighted graph implementation."""

    def __init__(self, vertices: List[int], edges: List[Tuple[int, int, int]]):
        """Initialize directed weighted graph.

        Args:
            vertices: list of vertices.
            edges: list of edges.
        """
        super().__init__(vertices, edges)
        self._adjacency_list = self._get_adjacency_list(vertices, edges)
        self._edges = self._get_edges(vertices, edges)

    def _get_adjacency_list(
        self, vertices: List[int], edges: List[Tuple[int, int, int]]
    ) -> Dict[int, List[int]]:
        adjacency_list = {vertex: [] for vertex in vertices}
        for edge in edges:
            adjacency_list[edge[0]].append((edge[1], edge[2]))
        return adjacency_list

    def _get_edges(
        self, vertices: List[int], edges: List[Tuple[int, int, int]]
    ) -> List[Tuple[int, int]]:
        return [(edge[0], edge[1]) for edge in edges]

    def _topological_sort_util(self, vertex: int, visited: Set[int], stack: List[int]):
        visited.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                self._topological_sort_util(adjacent_vertex, visited, stack)
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
                self._topological_sort_util(vertex, visited, stack)
        return stack[::-1]

    def _is_cyclic_util(self, vertex: int, visited: Set[int], stack: Set[int]) -> bool:
        visited.add(vertex)
        stack.add(vertex)
        for adjacent_vertex in self._adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                if self._is_cyclic_util(adjacent_vertex, visited, stack):
                    return True
            elif adjacent_vertex in stack:
                return True
        stack.remove(vertex)
        return False

    def is_cyclic(self) -> bool:
        """Check if graph is cyclic"""
        visited = set()
        stack = set()
        for vertex in self._vertices:
            if vertex not in visited:
                if self._is_cyclic_util(vertex, visited, stack):
                    return True
        return False


if __name__ == "__main__":
    graph = Graph(
        [0, 1, 2, 3, 4, 5], [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    )
    print(graph)
    print(graph.breadth_first_search(0))
    print(graph.depth_first_search(0))
    print(graph.topological_sort())
    print(graph.is_cyclic())
    print(graph.is_bipartite())
    print(graph.dijkstra(0))
    print(graph.bellman_ford(0))
