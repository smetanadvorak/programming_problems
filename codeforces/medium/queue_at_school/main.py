import sys, operator, functools

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
	n, t = tuple(map(int, f.readline().split()))
	repartition = list(f.readline()[:n])
	
# Solution here:
def gentlemen(repartition, t):	
	if len(repartition) <= 1:
		return repartition
	
	new_repartition = repartition[:]
	for i in range(t):
		for n in range(1,len(repartition)):
			if  repartition[n-1]=='B' and repartition[n]=='G':
				new_repartition[n-1] = 'G'
				new_repartition[n]   = 'B'	
		repartition = new_repartition[:]
		
	return repartition

repartition = gentlemen(repartition, t)
repartition = functools.reduce(operator.concat, repartition)

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(repartition)