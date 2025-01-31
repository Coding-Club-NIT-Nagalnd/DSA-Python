from typing import Any, Optional

class HashTable:
    def __init__(self, size: int) -> None:
        """
        Initialize a hash table with a fixed size.

        Parameters:
        - size: The size of the hash table.
        """
        self.size = size
        self.table: List[Optional[List[tuple[Any, Any]]]] = [None] * size  # List of buckets

    def _hash(self, key: Any) -> int:
        """
        Compute the hash value for a given key.

        Parameters:
        - key: The key to hash.

        Returns:
        - int: The hash value (index in the table).
        """
        pass

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert a key-value pair into the hash table.

        Parameters:
        - key: The key to insert.
        - value: The value associated with the key.
        """
        pass

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve the value associated with a key.

        Parameters:
        - key: The key to search for.

        Returns:
        - Optional[Any]: The value associated with the key, or None if the key is not found.
        """
        pass

    def delete(self, key: Any) -> None:
        """
        Delete a key-value pair from the hash table.

        Parameters:
        - key: The key to delete.
        """
        pass

    def contains(self, key: Any) -> bool:
        """
        Check if a key exists in the hash table.

        Parameters:
        - key: The key to check.

        Returns:
        - bool: True if the key exists, False otherwise.
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the hash table.

        Returns:
        - str: A string representation of the hash table.
        """
        pass