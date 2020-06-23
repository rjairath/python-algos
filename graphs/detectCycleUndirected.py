from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicUtil(self, node, visited, parent):
        visited[node] = True

        for adjNode in self.graph[node]:
            if not visited[adjNode]:
                if self.isCyclicUtil(adjNode, visited, node):
                    return True
            elif adjNode != parent:
                return True

        return False

    def isCyclic(self):
        visited = [False]*len(self.graph)

        for node in self.graph:
            if not visited[node]:
                if self.isCyclicUtil(node, visited, -1):
                    return True
        return False


g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(1, 2)


if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
