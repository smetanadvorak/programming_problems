#https://codeforces.com/contest/742/problem/C

# The citizens of Arpa's land form a directed graph
# The solution is possible if:
# 1) If all citizens are parts of cycles
# 2) All cycles are have the same length, 1-long cycles are always allowed

# Strategy: Find cycles until all citizens are accounted or until an uneven or new-size cycle appears

with open('input.txt', 'r') as f:
	n = int(f.readline())
	crush = list(map(int, f.readline().split()))

def walk_cycle(graph, start):
	visited = []
	current = start
	circ = 0
	while True:
		visited.append(current)
		current = crush[current-1]
		if current in visited: #Detected a cycle
			if current == start:
				return visited #Did a full cycle
			else:
				return -1 #Didn't start in the cycle but got in it
						  #In this problem it means that some citizens are not part of a cycle.
		
		if len(visited) == len(graph):
			return -1 # If visited all elements and didn't detect a cycle.
		
		
def analyze_cycles(crush):
	notvisited = set([i+1 for i in range(len(crush))])
	lengths = [] # Initialise the length by the length of the first detected cycle
	while len(notvisited):
		visited = walk_cycle(crush, list(notvisited)[0])
		if visited != -1: #If a cycle detected
			notvisited = notvisited.difference(set(visited))
			lengths.append(len(visited))
		else:
			print('No solution (-1)')
			return -1

	maxlen = max(lengths)
	for l in lengths:
		if l != maxlen and l != 1 and (maxlen/l) % 2:
			print('No solution (-1)')
			return -1
				
	if maxlen % 2:
		print('t =', maxlen)
		return maxlen
	else:
		print('t =', maxlen/2)
		return maxlen/2

t = analyze_cycles(crush)
