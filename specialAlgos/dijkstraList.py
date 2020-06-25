# using adjacency list, undirected graph
from collections import defaultdict
from sys import maxsize
from minHeap import Heap


class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def addEdge(self, src, dest, w):
        newNode = [dest, w]
        self.graph[src].insert(0, newNode)

        newNode1 = [src, w]
        self.graph[dest].insert(0, newNode1)

    def minDist(self, dist, visited):
        min_dist = maxsize
        min_node = 0
        for i in range(self.V):
            if dist[i] < min_dist and not visited[i]:
                # print('temp', i)
                min_dist = dist[i]
                min_node = i

        return min_node

    def dijkstra(self, src):
        dist = [maxsize]*self.V
        visited = [False]*self.V

        dist[src] = 0
        # u is the index
        for count in range(self.V):
            u = self.minDist(dist, visited)
            visited[u] = True

            print('u.....', u)
            for adjNode in self.graph[u]:
                # print(u, adjNode, 'node....')
                nodeVertex = adjNode[0]
                edgeWeight = adjNode[1]

                if dist[nodeVertex] > dist[u] + edgeWeight and not visited[nodeVertex]:
                    # print('nodeVertex', nodeVertex)
                    dist[nodeVertex] = dist[u] + edgeWeight

        self.printSolution(dist)


# Driver program to test the above functions
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)

graph.dijkstra(0)
