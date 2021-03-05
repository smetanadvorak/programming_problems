#https://codeforces.com/problemset/problem/913/A
import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
	n = int(f.readline())
	m = int(f.readline())
	
	
# Solution here:
res = m & ( (1 << n) - 1 )
	

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(res))