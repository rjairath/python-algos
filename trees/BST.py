

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, currentRoot, new_val):

        if new_val < currentRoot.value:
            if currentRoot.left is None:
                currentRoot.left = Node(new_val)
            else:
                self.insert_helper(currentRoot.left, new_val)
        else:
            if currentRoot.right is None:
                currentRoot.right = Node(new_val)
            else:
                self.insert_helper(currentRoot.right, new_val)

    def printInorder(self):
        self.printInorderHelper(self.root)

    def printInorderHelper(self, currentRoot):
        if currentRoot:
            self.printInorderHelper(currentRoot.left)
            print(currentRoot.value)
            self.printInorderHelper(currentRoot.right)

    def search(self, find_val):
        return self.searchHelper(self.root, find_val)

    def searchHelper(self, currentRoot, find_val):
        if currentRoot is None:
            return False

        if currentRoot.value == find_val:
            return True

        if find_val < currentRoot.value:
            return self.searchHelper(currentRoot.left, find_val)

        else:
            return self.searchHelper(currentRoot.right, find_val)


# Set up tree
tree = BST(40)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

tree.printInorder()

# Check search
# Should be True
print(tree.search(4))
# # Should be False
print(tree.search(5))
