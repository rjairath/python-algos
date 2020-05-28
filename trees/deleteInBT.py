# delete a given node
from binaryTree import Node, printInorder


def deleteDeepest(root, node):
    # delete the rightmost node
    if root is None:
        return
    q = []
    q.append(root)
    while(len(q) > 0):
        temp = q.pop(0)
        if temp.left:
            if temp.left == node:
                temp.left = None
                return
            else:
                q.append(temp.left)
        if temp.right:
            if temp.right == node:
                temp.right = None
                return
            else:
                q.append(temp.right)


def deleteNode(root, key):
    # finds the key_node and calls deleteDeepest
    if root is None:
        return
    if root.left is None and root.right is None:
        if root.val == key:
            root = None
            return
        else:
            return

    key_node = None
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        temp = queue.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    if key_node:
        key_node.val = temp.val
        deleteDeepest(root, temp)
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

    printInorder(root)
    print('break')
    deleteNode(root, 2)
    printInorder(root)
