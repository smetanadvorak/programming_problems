# You're given a map of zeros and ones, where ones represent walls.
# Find a the shorest distance from top left corner (0,0) to bottom right corner
# (rows, cols), considering that you can demolish UP TO one of the walls.
# Start and finish are always 0, and initially there is always a valid way
# from start to finish. Nodes of the map are 4-connected, no diagonal passages.

# Write a function that takes the map and outputs the shortest distance taking
# into account the possibility to demolish one wall.

from collections import deque
from copy import deepcopy

def check_neighbours(map, node):
    # Checks which node's neighbours are passages
    R, C = len(map), len(map[0])
    res = []
    if node[1] < C-1: # Check right
        if not map[node[0]][node[1]+1]:
            res.append((node[0],node[1]+1))
    if node[1] > 0:   # Check left
        if not map[node[0]][node[1]-1]:
            res.append((node[0],node[1]-1))
    if node[0] < R-1: # Check down
        if not map[node[0]+1][node[1]]:
            res.append((node[0]+1,node[1]))
    if node[0] > 0:   # Check up
        if not map[node[0]-1][node[1]]:
            res.append((node[0]-1,node[1]))
    return res

def bfs(map):
    # Breadth-first search
    deq_nodes = deque()
    deq_dists = deque()
    deq_nodes.append((0,0))
    deq_dists.append(1)

    visited = []
    while deq_nodes:
        node = deq_nodes.popleft()
        dist = deq_dists.popleft()
        if not node in visited:
            visited.append(node)
            if node == (len(map)-1 , len(map[0])-1): # If at the finish
                return dist
            else:
                visited.append(node)
                neighbouring_passages = check_neighbours(map, node)
                for np in neighbouring_passages:
                    deq_nodes.append(np)
                    deq_dists.append(dist+1)
    return None


def get_remodeling_candidates(map):
    candidates = []
    for (i,row) in enumerate(map):
        for (j, elem) in enumerate(row):
            #If this is a wall
            if map[i][j]:
                neighbouring_passages = check_neighbours(map, (i,j))
                # If it may potentially be a shortcut
                if len(neighbouring_passages) > 1:
                    candidates.append((i,j))
    return candidates


def solution(map):
    dist = bfs(map)
    # If distance is already optimal, no need to change the map
    if dist <= len(map) + len(map[0]) - 1:
        return dist
    # If the distance is not optimal, find good walls and check what taking them down gives
    else:
        candidates = get_remodeling_candidates(map)
        dists = [dist]
        for c in candidates:
            map_remodeled = deepcopy(map)
            map_remodeled[c[0]][c[1]] = 0
            dists.append(bfs(map_remodeled))
        return min(dists)



print(solution([[0, 0],
                [0, 0]]), 3)

print(solution([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]), 6)

print(solution([[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]), 8)

print(solution([[0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0],
                [1, 1, 1, 0]]), 7)

print(solution([[0, 1, 1, 0],
                [0, 0, 0, 1],
                [1, 1, 0, 0]]), 6)

print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]), 11)


print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]), 10)

print(solution([[0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]), 11)
