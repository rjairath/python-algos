from binaryTree import printInorder


class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def insert(root, new_val):
    if root is None:
        root = Node(new_val)
        return
    else:
        if new_val < root.val:
            if root.left is None:
                root.left = Node(new_val)
            else:
                insert(root.left, new_val)
        else:
            if root.right is None:
                root.right = Node(new_val)
            else:
                insert(root.right, new_val)


# driver code
if __name__ == '__main__':
    root = Node(4)

    insert(root, 3)
    insert(root, 5)
    insert(root, 2)
    insert(root, 1)
    printInorder(root)
