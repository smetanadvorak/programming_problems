import sys

def euclid_algorithm(a,b):
	if not (a % b):
		return b
	if not (b % a):
		return a
	
	if a > b :
		c = a % b
		return euclid_algorithm(c, b)
	else :
		c = b % a
		return euclid_algorithm(c, a)


a = int(sys.argv[1])
b = int(sys.argv[2])

print(euclid_algorithm(b,a))

