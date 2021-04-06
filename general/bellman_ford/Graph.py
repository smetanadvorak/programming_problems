class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, frm, to, cost=0):
        if not frm in self.vertices:
            self.add_vertex(frm)

        if not to in self.vertices:
            self.add_vertex(to)

        self.vertices[frm][to] = cost
        self.vertices[to][frm] = cost
        self.edges.append({'from':frm, 'to':to, 'cost':cost})

    def get_vertices(self):
        return self.vertices.keys()

    def get_edges(self):
        return self.edges
