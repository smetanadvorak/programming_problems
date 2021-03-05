# You and your rescued bunny prisoners need to get out of this collapsing death trap of a space station - and fast! Unfortunately, some of the bunnies have been weakened by their long imprisonment and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close. 
#
# The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave - you can move to and from the bulkhead to pick up additional bunnies if time permits.
#
# In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.
#
# Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest prisoner IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.
#
# For instance, in the case of
# [
#   [0, 2, 2, 2, -1],  # 0 = Start
#   [9, 0, 2, 2, -1],  # 1 = Bunny 0
#   [9, 3, 0, 2, -1],  # 2 = Bunny 1
#   [9, 3, 2, 0, -1],  # 3 = Bunny 2
#   [9, 3, 2, 2,  0],  # 4 = Bulkhead
# ]
# and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:
#
# Start End Delta Time Status
#     -   0     -    1 Bulkhead initially open
#     0   4    -1    2
#     4   2     2    0
#     2   4    -1    1
#     4   3     2   -1 Bulkhead closes
#     3   4    -1    0 Bulkhead reopens; you and the bunnies exit
#
# With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the answer is [1, 2].



from collections import deque
import itertools
import math

def detect_loop(history):
	inds = [i for i in range(len(history)) if history[i]==history[-1]]
	if len(inds) >= 3:
		inds = inds[-3:-1] # Take last two
		if history[inds[0]:inds[1]] == history[inds[1]:-1]:
			return True
	return False

def dijkstra(graph, start, finish):
	# Allocate and initialise costs of nodes:
	for node in graph.keys():
		graph[node]['cost'] = float('inf')
	graph[start]['cost'] = 0

	history = deque([], len(graph.keys())*2+1) # For loop detection.
										  #	Length is limited to twice the length of the longest possible loop plus one.

	# Dijkstra with negative weights
	to_visit = set([start])
	while to_visit:
		node = min(to_visit, key=lambda n: graph[n]['cost']) # Normal step: take the closest node.
		to_visit.remove(node)

		# Detection of loops with positive net time gain.
		# If there is one, the shortest path is -inf long and all bunnies can be rescued. Exit.
		history.append(node)		# Fill the visit history for loop detection.
		if detect_loop(list(history)):
			return -float('inf')

		# If no loop, proceed normally.
		neighbours = list(graph[node].keys())[:-1] # In fact, neighbours is always [0,1,2,3 etc.], but this is bit more general
												   # [:-1] to exclude 'cost' key, which is always the last

		# If some of the neighbours' cost has changed, add it to the 'to_visit' list.
		for neighbour in neighbours:
			if graph[node]['cost'] + graph[node][neighbour] < graph[neighbour]['cost']:  # Calculate the costs for neighbours
				graph[neighbour]['cost'] = graph[node]['cost'] + graph[node][neighbour]  # If the path through this node is shorter, update the cost
				to_visit.add(neighbour) # This is the difference between normal Dijkstra and Dijkstra with negative weights

	return graph[finish]['cost']

def matrix2dict(A):
    graph = {}
    for (i,row) in enumerate(A):
        graph[i] = {}
        for (j,elem) in enumerate(row):
            graph[i][j] = elem
    return graph

def solution(A, T):
	# Get bunny indices
	bunnies = list(range(len(A)-2))
	# Convert matrix to graph (dictionary)
	graph = matrix2dict(A)
	finish = len(A) - 1
	start = 0

	# If a loop with infinite time gain detected, then all bunnies can be rescued.
	if dijkstra(graph, start, finish) == -float('inf'):
		return bunnies

	# Iterate through possible rescue orders (permutations of 'bunnies')
	# and ones that fit into the time limit.
	solutions = []
	perms = itertools.permutations(bunnies)
	for p in perms:
		start = 0
		time_left = T
		solution = []
		for bunny in p:
			# Go for the bunny
			time_left -= dijkstra(graph, start, bunny+1)
			start = bunny + 1

			# If you can reach the exit from here in time, add it as a solution
			if time_left - dijkstra(graph, bunny+1, finish)	>= 0:
				solution.append(bunny)
				solutions.append(''.join(map(str,sorted(solution))))

	if len(solutions):
		maxlen = len(max(solutions, key=lambda p: len(p)))
		# Get all solutions with the maximum number of rescued bunnies
		solutions = [s for s in solutions if len(s)==maxlen]
		# Get the solution with highest alphabetical order (output requirement).
		solution = min(solutions)
		# Convert to list and return
		return list(map(int, list(solution)))
	else:
		return []


A = [[0, 2, 2, 2, -1],  # 0 = Start
  	 [9, 0, 2, 2, -1],  # 1 = Bunny 0
  	 [9, 3, 0, 2, -1],  # 2 = Bunny 1
  	 [9, 3, 2, 0, -1],  # 3 = Bunny 2
  	 [9, 3, 2, 2,  0]]  # 4 = Bulkhead
T = 1
print(solution(A, T))

A = [[0, 1, 1, 1, 1],
	 [1, 0, 1, 1, 1],
	 [1, 1, 0, 1, 1],
	 [1, 1, 1, 0, 1],
	 [1, 1, 1, 1, 0]]
T = 3
print(solution(A, T))

A = [[0, 1, 1],
	 [1, 0, 1],
	 [1, 1, 0]]
T = 1
print(solution(A, T))

T = 2
print(solution(A, T))

A = [[0, 1, -2],
	 [1, 0, 1],
	 [1, 1, 0]]
T = 1
print(solution(A, T))
