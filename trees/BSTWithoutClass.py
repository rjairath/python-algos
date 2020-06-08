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


def findMin(root):
    # find the leftmost node
    temp = root
    while(temp.left):
        temp = temp.left
    print('min', temp.val)
    return temp


def deleteNode(root, key):
    # Given a binary search tree and a key, this function
    # delete the key and returns the new root
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    # this is the node to be deleted
    else:
        deleteNode
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        else:
            # both exist
            # find inorder successor and replace it with this one
            temp = findMin(root.right)
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)

    return root


# driver code
if __name__ == '__main__':
    root = Node(50)

    insert(root, 30)
    insert(root, 70)
    insert(root, 20)
    insert(root, 40)
    insert(root, 60)
    insert(root, 80)
    # printInorder(root)

    # test delete
    print('delete')
    new_root = deleteNode(root, 30)
    printInorder(new_root)
