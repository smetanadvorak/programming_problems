#https://codeforces.com/contest/742/problem/E
# This is a graph colouring problem. If graph can be coloured in two colors, then there is a solution.
# Use greedy algorithm to color the graph. 
import sys
from collections import deque

with open('input.txt', 'r') as f:
	p = int(f.readline())
	n = 2*p
	graph = {i+1 : [(i+1)%n + 1 , (i-1)%n + 1] for i in range(n)} #Cyclic undirected graph
	boys = []
	girls = []
	for i in range(p):
		a, b = tuple(map(int, f.readline().split()))
		graph[a].append(b)
		graph[b].append(a)
		boys.append(a)
		girls.append(b)
		
		
def greedy_coloring(graph):
	colors = {key : 0 for key in graph.keys()} # Gray color everywhere
	visited = []	
	toprocess = deque([list(graph.keys())[0]]) # Start in the first node of the graph
	
	while toprocess:
		node = toprocess.popleft()
		visited.append(node)
		neighbours_colors = [colors[neighbour] for neighbour in graph[node]]
		if all(color != 1 for color in neighbours_colors):
			colors[node] = 1
		elif all(color != 2 for color in neighbours_colors):
			colors[node] = 2
		else :
			return -1
	
		for neighbour in graph[node]:
			if not neighbour in visited:
				toprocess.append(neighbour)
			
	return colors

colors = greedy_coloring(graph)
if colors == -1:
	print(-1)
else:
	for pair in range(p):
		print(colors[boys[pair]], colors[girls[pair]])
	