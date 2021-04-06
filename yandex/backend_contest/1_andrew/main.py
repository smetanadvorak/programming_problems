import sys

# Get the input file
assert len(sys.argv) > 1
inputname = sys.argv[1]

# Read input
with open(inputname, 'r') as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))


# Solution here:
def solution(a):
    if len(a) == 1:
        return 0
    if any([a[i-1]>a[i] for i in range(1, len(a))]): # If the list is not increasing
        return -1
    return a[-1] - a[0]
    #for i in range(len(a)-2, -1, -1):


# Write to the output file
outputname = inputname[0:-3] + '.res'
with open(outputname, 'w') as f:
	f.write(str(solution(a))+'\n')


# OK
# # Read input
# with open('input.txt', 'r') as f:
#     n = int(f.readline())
#     a = list(map(int, f.readline().split()))
#
#
# def solution(a):
#     if len(a) == 1:
#         return 0
# 	# If the list is decreasing somewhere, impossible to equalize volumes
#     if any([a[i-1]>a[i] for i in range(1, len(a))]):
#         return -1
#     return a[-1] - a[0] #Takes this much to equalize volumes
#
# with open('output.txt', 'w') as f:
# 	f.write(str(solution(a)))
