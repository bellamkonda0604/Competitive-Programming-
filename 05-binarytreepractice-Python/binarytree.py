class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the find_val is in the tree and False otherwise.
        """
        # Your code goes here
        if self.root is not None:
            return self.find(find_val, self.root)
        else:
            return False


    def find(self, val, node):
        if node:
            if val == node.value:
                return True
            else:
                return False
            return self.find(val, node.left)
            return self.find(val, node.right) 

    def print_tree(self, node):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        if node is not None:
            self.print_tree(node.left)
            print(str(node.value) + ' ')
            self.print_tree(node.right)
        

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        if self.root is not None:
            self.print_tree(self.root)
        

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        if self.root is not None:
            self.print_tree(self.root)