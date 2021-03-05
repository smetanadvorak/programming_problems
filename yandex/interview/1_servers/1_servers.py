import sys
from functools import reduce

filename = 'input.txt'

# with open(filename, 'r') as f:
# 	n = int(f.readline())
# 	a = [None] * n 
# 	b = [None] * n
# 	i = 0
# 	for line in f:
# 		a[i], b[i] = tuple(elem/100 for elem in map(int, line.split()))
# 		i += 1

with open(filename, 'r') as f:
	n = int(f.readline())
	a = []
	b = []
	for line in f:
		parced = list(map(int, line.split()))
		a.append(parced[0]/100)
		b.append(parced[1]/100)
		
filename = 'input.txt'

	
def calc_prob(a, b):
	likelihood = list(map(lambda x,y:x*y, a, b))
	total_prob = sum(likelihood)
	return [l/total_prob for l in likelihood]

[print(elem) for elem in calc_prob(a,b)]

