from typing import List, Optional

class MinHeap:
    def __init__(self) -> None:
        """
        Initialize a min-heap.
        """
        self.heap: List[int] = []  # List to store heap elements

    def parent(self, index: int) -> Optional[int]:
        """
        Get the parent index of a given index.

        Parameters:
        - index: The index of the current node.

        Returns:
        - Optional[int]: The parent index, or None if the index is invalid.
        """
        pass

    def left_child(self, index: int) -> Optional[int]:
        """
        Get the left child index of a given index.

        Parameters:
        - index: The index of the current node.

        Returns:
        - Optional[int]: The left child index, or None if the index is invalid.
        """
        pass

    def right_child(self, index: int) -> Optional[int]:
        """
        Get the right child index of a given index.

        Parameters:
        - index: The index of the current node.

        Returns:
        - Optional[int]: The right child index, or None if the index is invalid.
        """
        pass

    def insert(self, value: int) -> None:
        """
        Insert a value into the heap.

        Parameters:
        - value: The value to insert.
        """
        pass

    def extract_min(self) -> Optional[int]:
        """
        Extract and return the minimum value from the heap.

        Returns:
        - Optional[int]: The minimum value, or None if the heap is empty.
        """
        pass

    def heapify_up(self, index: int) -> None:
        """
        Restore the heap property by moving a node up the heap.

        Parameters:
        - index: The index of the node to move up.
        """
        pass

    def heapify_down(self, index: int) -> None:
        """
        Restore the heap property by moving a node down the heap.

        Parameters:
        - index: The index of the node to move down.
        """
        pass

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        Returns:
        - bool: True if the heap is empty, False otherwise.
        """
        pass

    def size(self) -> int:
        """
        Get the number of elements in the heap.

        Returns:
        - int: The number of elements in the heap.
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the heap.

        Returns:
        - str: A string representation of the heap.
        """
        pass