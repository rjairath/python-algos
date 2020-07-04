# find the first shortest root to leaf path
class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def printStack(stack):
    while(len(stack) > 0):
        print(stack.pop(), end=" ")


def printPath(data, parent, ans):
    if data == parent[data]:
        ans.append(data)
        printStack(ans)
        return
    ans.append(data)
    printPath(parent[data], parent, ans)


def leftMostShortest(root):
    parent = {}
    parent[root.data] = root.data
    leafNode = None

    q = []
    q.append(root)

    ans = []

    while(len(q) > 0):
        temp = q.pop(0)
        if not temp.left and not temp.right:
            leafNode = temp.data
            printPath(leafNode, parent, ans)
            break

        if temp.left:
            q.append(temp.left)
            parent[temp.left.data] = temp.data

        if temp.right:
            q.append(temp.right)
            parent[temp.right.data] = temp.data


def BFS(root):
    q = []
    q.append(root)

    while(len(q) > 0):
        temp = q.pop(0)
        print(temp.data, end=" ")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    print()


def DFS(root):
    # inorder
    if root is None:
        return
    DFS(root.left)
    print(root.data, end=" ")
    DFS(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(10)
    root.left.left.right = Node(11)
    root.right.right.left = Node(8)

    leftMostShortest(root)
    # DFS(root)
