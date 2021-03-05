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
	
# Brute force solution here:
def lexicographic_geq(s1, s2):
	i = 0
	while i < len(s1) and i < len(s2):
		if s1[i] > s2[i]:
			return True
		if s2[i] > s1[i]:
			return False
		i += 1
	#		
	if len(s1) >= len(s2):
		return True
	if len(s2) > len(s1):
		return False
		
def bruteforce(string):
	minstr = string
	for c in range(len(string)):
		s = string[:c] + string[c+1:]
		if s < minstr: #lexicographic_geq(minstr, s): #
			minstr = s
	#			
	return minstr

def minimize_string(string):
	string += ' '
	for i in range(1,len(string)):
		if string[i-1] > string[i]:
			string = string[:i-1] + string[i:]
			break
	#
	return string[:-1]
	
	
#res = minimize_string(string)
res = bruteforce(string)

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(res + '\n')