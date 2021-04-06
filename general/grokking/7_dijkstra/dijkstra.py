from collections import deque
import math

# The graph: children and costs
G = {} 
G["B"] = {"L":5, "P":0}
G["P"] = {"D":35, "G":30}
G["D"] = {"K":10}
G["G"] = {"K":20}
G["L"] = {"G":15, "D":20}
G["K"] = {}

start = "B"
finish = "K"

def get_smallest_cost_node(C, processed):
	smallest_cost_node = None
	smallest_cost = math.inf
	
	for node in C:
		if (not node in processed) and (C[node] < smallest_cost):
			smallest_cost_node = node
			smallest_cost = C[node]
	
	return smallest_cost_node
	

def dijkstra(G, start, finish):
	# Allocate and initialise costs of nodes:
	C = {}
	for node in G.keys():
		if node == start:
			C[node] = 0
		else:
			C[node] = math.inf
		
	# Allocate parents of nodes:
	P = {}
	P[start] = {}
	processed = []
	
	# Algorithm
	node = start
	while node is not None:	
		processed.append(node)
		neighbours = G[node].keys()
		for neighbour in neighbours:
			if G[node][neighbour] + C[node] < C[neighbour]:  # Calculate the costs for neighbours
				C[neighbour] = G[node][neighbour] + C[node]	 # If the path through this node is shorter, update the cost
				P[neighbour] = node
				
		node = get_smallest_cost_node(C, processed)

	# Get resulting path
	path = [finish]
	while P[path[-1]]:
		path.append(P[path[-1]])
		
	return path[::-1]
	
print(dijkstra(G, start, finish))

	
	