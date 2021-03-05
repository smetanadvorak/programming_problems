import sys
from collections import deque

# Read the input
with open('input.txt', 'r') as f:
	nhoses, npairs, maxweight = tuple(map(int, f.readline().split()))
	weights =  list(map(int, f.readline().split()))
	beauties = list(map(int, f.readline().split()))
	friendship = {hos+1 : [] for hos in range(nhoses)}
	for i in range(npairs):
		a, b = tuple(map(int, f.readline().split()))
		friendship[a].append(b)
		friendship[b].append(a)
		
print(friendship)

def breadth_component_search(graph, start):
	# Function that does a bfs over a graph starting in start
	component = []
	tovisit = deque([start])
	
	while tovisit:
		vertex = tovisit.popleft()
		component.append(vertex)
		for friend in graph[vertex]:
			if not (friend in component):
				tovisit.append(friend)
	
	return component
	
# Find all connected components of the graph:
groups = {}
notvisited = set(range(1,nhoses+1))

i = 1
while len(notvisited):
	vertex = list(notvisited)[0]
	component = breadth_component_search(friendship, vertex)
	components[i] = component
	i += 1
	notvisited = notvisited.difference(component)
	
print(groups)

# Add total weights and total beauties of the groups into the corresponding vectors
for key in groups.keys():
	weights.append(sum(weights[i] for i in groups[key]))
	beauties.append(sum(beauties[i] for i in groups[key]))
	

		