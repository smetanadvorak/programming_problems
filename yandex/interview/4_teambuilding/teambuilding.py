from collections import deque

# Find all nodes of a clique
def get_connected_component(graph, node):
	cc = set([node])
	visited = set([node])
	to_visit = set(graph[node])
	while len(to_visit):
		current_node = to_visit.pop()
		visited.add(current_node)
		if set(graph[current_node]).issuperset(cc):
			cc.add(current_node)
			to_visit.update(graph[current_node])
	return cc

# Find n cliques in the graph
def find_n_connected_components(graph, n_groups = 2):
	for n in range(n_groups):
		if len(graph) == 0:
			return False
		seed = next(iter(graph.keys()))
		connected_component = get_connected_component(graph, seed)
		for c in connected_component:
			del graph[c]

	return len(graph)==0

with open('input.txt', 'r') as f:
	n,m = map(int, f.readline().split())
	graph = {i+1:set([]) for i in range(n)}
	for i in range(m):
		node1, node2 = map(int, f.readline().split())
		graph[node1].add(node2)
		graph[node2].add(node1)

print(find_n_connected_components(graph))
