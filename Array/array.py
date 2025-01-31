class Array:
    def __init__(self, size: int) -> None:
        """
        Initialize an array with a fixed size.

        Parameters:
        - size: The size of the array.
        """
        self.size = size
        self.data = [None] * size  # Initialize array with `None` values

    def get(self, index: int) -> int:
        """
        Get the value at a specific index in the array.

        Parameters:
        - index: The index to retrieve the value from.

        Returns:
        - int: The value at the specified index.
        """
        pass

    def set(self, index: int, value: int) -> None:
        """
        Set a value at a specific index in the array.

        Parameters:
        - index: The index where the value will be set.
        - value: The value to be set at the specified index.
        """
        pass

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a specific index in the array. Shifts elements to the right.

        Parameters:
        - index: The index where the value will be inserted.
        - value: The value to be inserted.
        """
        pass

    def delete(self, index: int) -> None:
        """
        Delete the value at a specific index in the array. Shifts elements to the left.

        Parameters:
        - index: The index of the value to be deleted.
        """
        pass

    def search(self, value: int) -> int:
        """
        Search for a value in the array and return its index.

        Parameters:
        - value: The value to search for.

        Returns:
        - int: The index of the value if found, otherwise -1.
        """
        pass

    def length(self) -> int:
        """
        Get the number of elements in the array.

        Returns:
        - int: The number of elements in the array.
        """
        pass

    def is_empty(self) -> bool:
        """
        Check if the array is empty.

        Returns:
        - bool: True if the array is empty, False otherwise.
        """
        pass

    def is_full(self) -> bool:
        """
        Check if the array is full.

        Returns:
        - bool: True if the array is full, False otherwise.
        """
        pass

    def resize(self, new_size: int) -> None:
        """
        Resize the array to a new size.

        Parameters:
        - new_size: The new size of the array.
        """
        pass

    def reverse(self) -> None:
        """
        Reverse the elements of the array in place.
        """
        pass

    def sort(self) -> None:
        """
        Sort the elements of the array in ascending order.
        """
        pass

    def __str__(self) -> str:
        """
        Return a string representation of the array.

        Returns:
        - str: A string representation of the array.
        """
        pass