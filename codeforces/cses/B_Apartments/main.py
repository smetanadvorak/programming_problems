# https://codeforces.com/gym/102961/problem/B

import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
    n,m,k = tuple(map(int, f.readline().split()))
    a = list(map(int, f.readline().split())) # Desired sizes
    b = list(map(int, f.readline().split())) # Available sizes

# Solution here:
result = 0
for apartment in range(m):
    if len(a) == 0:
        break
    discrepancy = [abs(desired - b[apartment]) for desired in a]
    closest_applicant = min(range(len(discrepancy)), key = discrepancy.__getitem__)
    if discrepancy[closest_applicant] <= k:
        result += 1
        del a[closest_applicant] # Remove the happy applicant




# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(result)+'\n')
