from collections import deque

graph = {}
graph["you"] = ["bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["you"]
graph["claire"] = ["jonny", "thom"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []
graph["peggy"] = ["alice"]

def breadth_first_search(graph, start, finish):
	deq = deque()
	deq += graph[start]
		
	while deq:
		current_node = deq.popleft()
		if current_node == finish:
			return True
		else:
			deq += graph[current_node]
	
	return False


def breadth_first_dist(graph, start, finish):
	if start == finish:
		return True, 0
	
	# Loop protection	
	visited = [start]
	
	# Nodes deck
	deq_node = deque()
	deq_node += graph[start]
	
	# Distances deck
	deq_dist = deque()
	deq_dist += [1] * len(graph[start])
		
	while deq_node:
		current_node = deq_node.popleft()
		current_dist = deq_dist.popleft()
		
		if not current_node in visited:
			if current_node == finish:
				return True, current_dist
			else:
				visited.append(current_node)
				deq_node += graph[current_node]
				deq_dist += [current_dist+1] * len(graph[current_node])
	
	return False, None

start = "you"
finish = "you"
print(breadth_first_search(graph, start, finish))
print(breadth_first_dist(graph, start, finish))