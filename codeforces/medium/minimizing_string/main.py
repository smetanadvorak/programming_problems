#https://codeforces.com/problemset/problem/1076/A

import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
	n = int(f.readline())
	string = f.readline()

if string[-1] == '\n':
	string = string[:-1]
	
# Solution here:
def minimize_string(string):
	string += ' '
	for i in range(1,len(string)):
		if string[i-1] > string[i]:
			string = string[:i-1] + string[i:]
			break
	#
	return string[:-1]
	
res = minimize_string(string)

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(res + '\n')