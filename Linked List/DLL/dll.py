class Node:
    """
    Represents a node in a doubly linked list.
    
    Attributes:
        data (int): The value stored in the node.
        next (Node or None): Reference to the next node in the list.
        prev (Node or None): Reference to the previous node in the list.
    """
    def __init__(self, data: int) -> None:
        """
        Initializes a new node with given data and sets next and prev to None.
        
        Parameters:
            data (int): The value to be stored in the node.
        """
        pass


class DoublyLinkedList:
    """
    Represents a doubly linked list.
    
    Attributes:
        head (Node or None): Reference to the first node of the list.
    """
    def __init__(self) -> None:
        """
        Initializes an empty doubly linked list.
        """
        pass

    def insert_at_beginning(self, data: int) -> None:
        """
        Inserts a new node with the given data at the beginning of the list.
        
        Parameters:
            data (int): The value to be stored in the new node.
        """
        pass
    
    def insert_at_end(self, data: int) -> None:
        """
        Inserts a new node with the given data at the end of the list.
        
        Parameters:
            data (int): The value to be stored in the new node.
        """
        pass
    
    def insert_after_node(self, prev_node: Node, data: int) -> None:
        """
        Inserts a new node with the given data after the specified node.
        
        Parameters:
            prev_node (Node): The node after which the new node should be inserted.
            data (int): The value to be stored in the new node.
        """
        pass
    
    def delete_node(self, key: int) -> None:
        """
        Deletes the first node with the given key from the list.
        
        Parameters:
            key (int): The value to be deleted from the list.
        """
        pass
    
    def search(self, key: int) -> bool:
        """
        Searches for a node with the given key in the list.
        
        Parameters:
            key (int): The value to search for in the list.
        
        Returns:
            bool: True if the key is found, otherwise False.
        """
        pass
    
    def display(self) -> None:
        """
        Prints the elements of the list in order.
        """
        pass
    
    def reverse(self) -> None:
        """
        Reverses the linked list in place.
        """
        pass
    
    def get_length(self) -> int:
        """
        Returns the number of nodes in the linked list.
        
        Returns:
            int: The count of nodes in the list.
        """
        pass