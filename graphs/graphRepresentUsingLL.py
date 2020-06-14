class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount
        self.adjList = [None] * self.vertexCount
        self.visitedArray = [False] * self.vertexCount

    def addEdge(self, from_val, to_val):
        if self.adjList[from_val] is None:
            from_node = Node(from_val)
            self.adjList[from_val] = from_node

        to_node = Node(to_val)
        # insert at the head of LL as it is an O(1) operation
        # to_node.next = self.adjList[from_val]
        # self.adjList[from_val] = to_node

        # try inserting at end now
        temp = self.adjList[from_val]
        while(temp.next):
            temp = temp.next
        temp.next = to_node

    def printGraph(self):
        for i in range(self.vertexCount):
            temp = self.adjList[i]
            print('vertex ', i, ': ', end="")
            while(temp):
                print(temp.value, end="->")
                temp = temp.next
            print()

    def DFS(self, start_node_num):
        start_node = self.adjList[start_node_num]
        if self.visitedArray[start_node_num] == True:
            return
        self.visitedArray[start_node_num] = True
        print(start_node_num)

        temp = start_node.next
        while(temp):
            # print(temp.value, 'val.......')
            self.DFS(temp.value)
            temp = temp.next

    def BFS(self, start_node_num):
        start_node = self.adjList[start_node_num]
        queue = [start_node_num]
        self.visitedArray[start_node_num] = True

        while(len(queue) > 0):
            # item is a number
            item = queue.pop(0)
            print(item)

            temp = self.adjList[item]
            temp = temp.next
            while(temp):
                if self.visitedArray[temp.value] == False:
                    queue.append(temp.value)
                    self.visitedArray[temp.value] = True
                temp = temp.next


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.printGraph()
print('BFS: ')
g.BFS(2)
