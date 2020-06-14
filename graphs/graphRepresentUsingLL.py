class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount
        self.adjList = [None] * self.vertexCount

    def addEdge(self, from_val, to_val):
        to_node = Node(to_val)
        # insert at the head of LL as it is an O(1) operation
        to_node.next = self.adjList[from_val]
        self.adjList[from_val] = to_node

    def printGraph(self):
        for i in range(self.vertexCount):
            temp = self.adjList[i]
            print('vertex ', i, ': ', end="")
            while(temp):
                print(temp.value, end="->")
                temp = temp.next
            print()


graph = Graph(5)
graph.addEdge(0, 1)
graph.addEdge(0, 4)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 3)
graph.addEdge(3, 4)

graph.printGraph()
