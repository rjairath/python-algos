# Given an adjacency matrix representation of Graph,
# find the shortest distance of every vertex from
# the given vertex

import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, visited):
        min_dist = sys.maxsize
        min_node = 0
        for i in range(self.V):
            if dist[i] < min_dist and not visited[i]:
                min_dist = dist[i]
                min_node = i

        return min_node

    def dijkstra(self, start):
        visited = [False]*self.V
        dist = [sys.maxsize]*self.V
        dist[start] = 0

        for counter in range(self.V):
            u = self.minDistance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and dist[v] > dist[u] + self.graph[u][v] and not visited[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


g = Graph(9)


g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
