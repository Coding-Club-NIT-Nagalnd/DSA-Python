class Node:
    def __init__(self, data: int) -> None:
        """
        Initializes a node with data and a pointer to the next node.
        
        Parameters:
        data (int): The value stored in the node.
        """
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        """
        Initializes an empty stack using a linked list.
        """
        self.top = None
        self._size = 0

    def push(self, item: int) -> None:
        """
        Adds an item to the top of the stack.
        
        Parameters:
        item (int): The item to be pushed onto the stack.
        """
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self) -> int:
        """
        Removes and returns the top item from the stack.
        
        Returns:
        int: The item that was removed from the stack.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def peek(self) -> int:
        """
        Returns the top item from the stack without removing it.
        
        Returns:
        int: The item at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.
        
        Returns:
        bool: True if the
        """