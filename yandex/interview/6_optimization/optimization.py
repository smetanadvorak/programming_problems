import sys

def distribute_roles(a,b):
	d = []
	for i in range(len(a)):
		d.append(a[i] - b[i])
	inds = sorted(range(len(d)), key=d.__getitem__)
	indsb = inds[:int(len(inds)/2)]
	indsa = inds[int(len(inds)/2):]
	value = sum(a[i] for i in indsa ) + sum(b[i] for i in indsb)
	
	return value

with open('input.txt', 'r') as f:
	n = int(f.readline())
	a = list(map(int, f.readline().split()))
	b = list(map(int, f.readline().split()))
	value = distribute_roles(a,b)
	# Read certificates
	c = int(f.readline())
	for i in range(c):
		employee, skill, upgrade = tuple(map(int, f.readline().split()))
		if skill == 1:
			a[employee-1] += upgrade  
		elif skill == 2:
			b[employee-1] += upgrade	
	
		value = distribute_roles(a,b)
		print(value)
		
		
