class BinaryTreeNode:
    def __init__(self, value: int) -> None:
        """
        Initialize a node in the binary tree.

        Parameters:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        """
        Initialize an empty binary tree.
        """
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert a value into the binary tree.

        Parameters:
        - value: The value to be inserted into the tree.
        """
        pass

    def delete(self, value: int) -> None:
        """
        Delete a value from the binary tree.

        Parameters:
        - value: The value to be deleted from the tree.
        """
        pass

    def search(self, value: int) -> bool:
        """
        Search for a value in the binary tree.

        Parameters:
        - value: The value to search for in the tree.

        Returns:
        - bool: True if the value is found, False otherwise.
        """
        pass

    def inorder_traversal(self) -> list[int]:
        """
        Perform an in-order traversal of the binary tree.

        Returns:
        - list: A list of values in in-order sequence.
        """
        pass

    def preorder_traversal(self) -> list[int]:
        """
        Perform a pre-order traversal of the binary tree.

        Returns:
        - list: A list of values in pre-order sequence.
        """
        pass

    def postorder_traversal(self) -> list[int]:
        """
        Perform a post-order traversal of the binary tree.

        Returns:
        - list: A list of values in post-order sequence.
        """
        pass

    def level_order_traversal(self) -> list[int]:
        """
        Perform a level-order (breadth-first) traversal of the binary tree.

        Returns:
        - list: A list of values in level-order sequence.
        """
        pass

    def height(self) -> int:
        """
        Calculate the height of the binary tree.

        Returns:
        - int: The height of the tree.
        """
        pass

    def size(self) -> int:
        """
        Calculate the number of nodes in the binary tree.

        Returns:
        - int: The number of nodes in the tree.
        """
        pass

    def is_empty(self) -> bool:
        """
        Check if the binary tree is empty.

        Returns:
        - bool: True if the tree is empty, False otherwise.
        """
        pass

    def find_min(self) -> int:
        """
        Find the minimum value in the binary tree.

        Returns:
        - int: The minimum value in the tree.
        """
        pass

    def find_max(self) -> int:
        """
        Find the maximum value in the binary tree.

        Returns:
        - int: The maximum value in the tree.
        """
        pass

    def is_bst(self) -> bool:
        """
        Check if the binary tree is a binary search tree (BST).

        Returns:
        - bool: True if the tree is a BST, False otherwise.
        """
        pass

    def balance_tree(self) -> 'BinaryTree':
        """
        Balance the binary tree to ensure optimal performance.

        Returns:
        - BinaryTree: A new balanced binary tree.
        """
        pass