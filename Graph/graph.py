from typing import Dict, List, Optional

class Graph:
    def __init__(self, directed: bool = False) -> None:
        """
        Initialize a graph.

        Parameters:
        - directed: If True, the graph is directed. If False, the graph is undirected.
        """
        self.graph: Dict[int, List[int]] = {}  # Adjacency list representation
        self.directed = directed

    def add_vertex(self, vertex: int) -> None:
        """
        Add a vertex to the graph.

        Parameters:
        - vertex: The vertex to be added.
        """
        pass

    def remove_vertex(self, vertex: int) -> None:
        """
        Remove a vertex from the graph.

        Parameters:
        - vertex: The vertex to be removed.
        """
        pass

    def add_edge(self, vertex1: int, vertex2: int) -> None:
        """
        Add an edge between two vertices in the graph.

        Parameters:
        - vertex1: The first vertex.
        - vertex2: The second vertex.
        """
        pass

    def remove_edge(self, vertex1: int, vertex2: int) -> None:
        """
        Remove an edge between two vertices in the graph.

        Parameters:
        - vertex1: The first vertex.
        - vertex2: The second vertex.
        """
        pass

    def has_vertex(self, vertex: int) -> bool:
        """
        Check if a vertex exists in the graph.

        Parameters:
        - vertex: The vertex to check.

        Returns:
        - bool: True if the vertex exists, False otherwise.
        """
        pass

    def has_edge(self, vertex1: int, vertex2: int) -> bool:
        """
        Check if an edge exists between two vertices.

        Parameters:
        - vertex1: The first vertex.
        - vertex2: The second vertex.

        Returns:
        - bool: True if the edge exists, False otherwise.
        """
        pass

    def get_neighbors(self, vertex: int) -> List[int]:
        """
        Get the neighbors of a vertex.

        Parameters:
        - vertex: The vertex to get neighbors for.

        Returns:
        - List[int]: A list of neighboring vertices.
        """
        pass

    def depth_first_search(self, start_vertex: int) -> List[int]:
        """
        Perform a depth-first search (DFS) starting from a vertex.

        Parameters:
        - start_vertex: The vertex to start the DFS from.

        Returns:
        - List[int]: A list of vertices visited during DFS.
        """
        pass

    def breadth_first_search(self, start_vertex: int) -> List[int]:
        """
        Perform a breadth-first search (BFS) starting from a vertex.

        Parameters:
        - start_vertex: The vertex to start the BFS from.

        Returns:
        - List[int]: A list of vertices visited during BFS.
        """
        pass

    def is_connected(self) -> bool:
        """
        Check if the graph is connected.

        Returns:
        - bool: True if the graph is connected, False otherwise.
        """
        pass

    def shortest_path(self, start_vertex: int, end_vertex: int) -> Optional[List[int]]:
        """
        Find the shortest path between two vertices.

        Parameters:
        - start_vertex: The starting vertex.
        - end_vertex: The ending vertex.

        Returns:
        - Optional[List[int]]: A list of vertices representing the shortest path, or None if no path exists.
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the graph.

        Returns:
        - str: A string representation of the graph.
        """
        pass