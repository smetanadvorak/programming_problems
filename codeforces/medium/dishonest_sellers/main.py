#Dishonest Sellers
#https://codeforces.com/problemset/problem/779/C

import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
	n, k = tuple(map(int, f.readline().split()))
	a = list(map(int, f.readline().split()))
	b = list(map(int, f.readline().split()))
	
assert(len(a)==len(b))
	
# Solution here:
def minimize_spendings(n, k, a, b):

	c = [a[i] - b[i] for i in range(len(a))]

	inds = sorted(range(len(c)), key=lambda k:c[k])
	c = [c[i] for i in inds]

	honest = 0
	while honest < len(a) and c[honest] <= 0:
		honest += 1
	
	k = max(k, honest)	
	
	during = inds[:k]
	after = inds[k:]

	return sum(a[i] for i in during) + sum(b[i] for i in after)


res = minimize_spendings(n, k, a, b)
print(res)

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(res))