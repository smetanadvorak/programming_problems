import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
	str = f.readline()
	
# Solution here:
i = 0

result = True
counter = 0
while i < len(str):
	if str[i] == '1':
		counter = 2
	else:
		if str[i] == '4':
			counter -= 1
			if counter < 0:
				result = False
				break
		else:
			result = False
			break
	
	i+=1
	
if not len(str):
	result = False
		
	

# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	if result:
		f.write('YES')
	else: 
		f.write('NO')