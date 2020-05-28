# Given a Binary Node and a node.
# The task is to search and check if the given node exits in the binary tree or not.
# If it exists, print YES otherwise print NO.
from binaryTree import Node, printInorder


def searchNode(root, x):
    if root is None:
        return False

    if root.val == x:
        return True

    l = searchNode(root.left, x)
    r = searchNode(root.right, x)

    return l or r


def insertNode(root, node):
    # insert on the first available left or right child in a BFS manner
    if root is None:
        root = node
        return
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        temp_node = queue.pop(0)
        if temp_node.left:
            queue.append(temp_node.left)
        else:
            temp_node.left = node
            return
        if temp_node.right:
            queue.append(temp_node.right)
        else:
            temp_node.right = node
            return


# driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # print('Inorder traversal: ')
    # printInorder(root)

    # if(searchNode(root, 400)):
    #     print('YES')
    # else:
    #     print('NO')
    new_node = Node(100)
    insertNode(root, new_node)
    printInorder(root)
