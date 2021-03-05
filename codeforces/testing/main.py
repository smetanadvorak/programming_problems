import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input and do calculations....
with open(inputname, 'r') as f:
	a = int(f.readline())

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(a+1))