class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val, root):
        # Your code goes here
        if root is None:
            return new_val
        else:
            if root.value == new_val:
                return root
            elif root.value < new_val:
                return find(new_val, root.right)
            else:
                return find( new_val, root.left)
        return root

    def printSelf(self, node):
        # Your code goes here
        if node is not None:
            self.printSelf(node.left)
            print(str(node.value) + ' ')
            self.printSelf(node.right)

        
    def search(self, find_val):
        # Your code goes here
        if self.root is not None:
            return self.find(find_val, self.root)
        else:
            return None

    def find(self, val, node):
        if node:
            if val == node.value:
                return True
            else:
                return False
            return self.find(val, node.left)
            return self.find(val, node.right)
        elif val < node.value and node.left is not None:
            return self.find(val, node.left)
        elif val > node.value and node.right is not None:
            return self.find(val, node.right)

