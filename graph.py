from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        if dest not in self.graph[src]:
            self.graph[src].append(dest)
        if src not in self.graph[dest]:
            self.graph[dest].append(src)
    
    def add_vertex(self, src):
        self.graph.setdefault(src, [])

    def __str__(self):
        return str(self.graph)

    def dfsUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for x in self.graph[v]:
            if x not in visited:
                self.dfsUtil(x, visited)

    def dfs(self, v=None):
        visited = set()
        if v is not None:
            self.dfsUtil(v, visited)
            print()
        else:
            for src in self.graph:
                if src not in visited:
                    self.dfsUtil(src, visited)
            print()

    def dfsWithStack(self, v):
        stack = [v]
        visited = set()
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)


    def bfs(self, v):
        queue = [v]
        visited = set()
        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current, end=' ')
                visited.add(current)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()




g = Graph()
g.add_edge(1, 3)
g.add_edge(0, 3)
g.add_edge(0, 1)
g.add_edge(2, 1)
g.add_edge(2, 5)
g.add_vertex(4)
g.add_vertex(2)

print(g)
print("------------------------------------------------------------------------")

g.dfs()
print("------------------------------------------------------------------------")

g.dfs(0)
print("------------------------------------------------------------------------")

g.dfs(1)
g.bfs(1)
print("------------------------------------------------------------------------")
