# 图数据结构的实现（无权重、无方向、节点不能重复）

# 图类
class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = []

    def size(self):
        return len(self.vertices)

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        if {v1, v2} not in self.edges:
            self.edges.append({v1, v2})

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)

    def trace(self):

        # deep first search
    def dfs(self):

        # breadth first search
    def bfs(self):
