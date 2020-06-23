from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicUtil(self, node, visited, parent):
        q = []
        q.append(node)
        visited[node] = True

        while(len(q) > 0):
            temp = q.pop(0)
            for adjNode in self.graph[temp]:
                if not visited[adjNode]:
                    q.append(adjNode)
                    visited[adjNode] = True
                    parent[adjNode] = temp

                elif adjNode != parent[temp]:
                    return True

        return False

    def isCyclic(self):
        visited = [False]*len(self.graph)
        parent = [-1]*len(self.graph)

        for node in self.graph:
            if not visited[node]:
                if self.isCyclicUtil(node, visited, parent):
                    return True

        return False


# Driver Code
if __name__ == "__main__":
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
