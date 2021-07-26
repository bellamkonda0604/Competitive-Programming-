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
        print(self.data)
        if self.value == find_val:
            return True
        if find_val < self.value:
            if self.left:
                self.left.search(find_val)
            else:
                return False    
        if find_val > self.value:
            if self.right:
                self.right.search(find_val)
            else:
                return False   

    def print_tree(self):
        """
        Print out all tree nodes as they are visited in a pre-order traversal."""
        # Your code goes here
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def preorder_search(self, start, find_val):
        """
        Helper method - use this to create a recursive search solution.
        """
        # Your code goes here
        res = []
        if start:
            res.append(start.value)
            res = res + self.PreorderTraversal(start.left)
            res = res + self.PreorderTraversal(start.right)
        return res

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a recursive print solution.
        """
        # Your code goes here
        return start.preorder_search(start)

print(BinaryTree(20))