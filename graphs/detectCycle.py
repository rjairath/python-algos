# detect cycle in a graph, (directed graph)

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        # V is the number of vertices
        self.graph = defaultdict(list)
        self. V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, index, visited, recStack):
        visited[index] = True
        recStack[index] = True

        for adjNode in self.graph[index]:
            if visited[adjNode] == False:
                if self.isCyclicUtil(adjNode, visited, recStack):
                    return True
            elif recStack[adjNode]:
                return True

        recStack[index] = False
        return False

    def isCyclic(self):
        visited = [False]*self.V
        recStack = [False]*self.V

        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack):
                    return recStack

        return recStack


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    # g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    # if g.isCyclic() == 1:
    #     print("Graph has a cycle")
    # else:
    #     print("Graph has no cycle")

    print(g.isCyclic())
