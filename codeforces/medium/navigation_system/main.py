import sys
from collections import deque

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
	n,m = tuple(map(int, f.readline().split())) 
	graph = {}
	for i in range(1,n+1):
		graph[i] = []
		
	for i in range(m):
		start, finish = tuple(map(int, f.readline().split()))
		graph[start].append(finish)
		
	l = int(f.readline())
	path = list(map(int,f.readline().split()))
	
# Solution here:
def find_shortest_paths(graph, start, finish):
	visited = start
	dnodes = deque()
	ddists = deque()
	dnodes += graph[start]
	ddists += [1]*len(graph[start])
	
	while dnodes:
		node = dnodes.popleft()
		dist = ddists.popleft()
		
		if not node in visited:
			if node == finish:
				return dist
			else:
				dnodes += graph(node)
				ddists += [dist+1]*len(graph(node))
				
	return None
	
def find_shortest_dist(graph, start, finish):
	visited = start
	
	dnodes = deque()
	ddists = deque()
	
	dnodes += graph[start]
	ddists += [1]*len(graph[start])
	
	while dnodes:
		node = dnodes.popleft()
		dist = ddists.popleft()
		
		if not node in visited:
			if node == finish:
				return dist
			else:
				dnodes += graph(node)
				ddists += [dist+1]*len(graph(node))
				
	return None
		
	
	
	

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(1))