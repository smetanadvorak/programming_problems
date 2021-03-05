import sys

def factorial(x):
	if x == 1:
		return 1
	else: 
		return factorial(x-1)*x

with open('input.txt', 'r') as f:
	n, x = tuple(map(int, f.readline().split()))
	a = list(map(int, f.readline().split()))

# Use the fact that if a xor b == x then a xor x = b
xa = [0 for i in range(len(a))]
for i in range(len(xa)):
	xa[i] = a[i]^x
	
# Make histogram 
hist = {}
for i in range(len(xa)):
	hist[str(xa[i])] = 0

for i in range(len(xa)):
	hist[str(xa[i])] += 1
	
answer = 0
for key in hist.keys():
	if hist[key] > 1:
		answer += factorial(hist[key])/2
		print(factorial(hist[key]))

print(xa)
print(hist)
print(answer)
