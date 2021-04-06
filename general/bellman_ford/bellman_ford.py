import math
from Graph import Graph

graph = Graph()

graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')

graph.add_edge('a','b',10)
graph.add_edge('b','c',-9)
graph.add_edge('a','c', 2)

def bellman_ford(graph, start):
    distance = {id: math.inf for id in graph.get_vertices()}
    distance[start] = 0
    predesessor = {id: None for id in graph.get_vertices()}

    for i in range(len(graph.get_vertices())):
        for edge in graph.get_edges():
            if distance[edge['from']] + edge['cost'] < distance[edge['to']]:
                predesessor[edge['to']] = edge['from']
                distance[edge['to']] = distance[edge['from']] + edge['cost']

    for edge in graph.get_edges():
        if distance[edge['from']] + edge['cost'] < distance[edge['to']]:
            raise "Graph contains a negative-weight cycle"

    return distance


print(bellman_ford(graph, 'a'))
