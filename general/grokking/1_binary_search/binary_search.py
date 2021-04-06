import sys

filename = sys.argv[1]
query = int(sys.argv[2])

# Read database from file
datafile = open(filename, 'r')

arr = []
for line in datafile:
	arr.append(int(line))

datafile.close()

# Binary search
def binary_search(data, query):
	if len(data) == 0:
		return 0

	mid = int(len(data)/2)
	
	if query == data[mid]:
		return mid + 1
		
	if query > data[mid]:
		res = binary_search(data[mid:], query)
		return (mid + res) * (res != 0)

	else: 
		res = binary_search(data[:mid], query)
		return (res) * (res != 0)
	

#arr = [1,2,3,4,5]
#query = 6

print(binary_search(arr, query))