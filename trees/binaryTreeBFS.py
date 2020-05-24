
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# calc height of BT
def height(root):
    if root == None:
        return 0
    lHeight = 1 + height(root.left)
    rHeight = 1 + height(root.right)

    return max(lHeight, rHeight)

def printGivenLevel(root, level):
    if root == None:
        return
    if level == 1:
        print(root.val)
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printLevelOrderUsingQueue(root):
    if root is None: 
        return
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        temp_node = queue.pop(0)
        print(temp_node.val)

        if temp_node:
            if temp_node.left is not None:
                queue.append(temp_node.left)
            if temp_node.right is not None:
                queue.append(temp_node.right)

# driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    printLevelOrderUsingQueue(root)
