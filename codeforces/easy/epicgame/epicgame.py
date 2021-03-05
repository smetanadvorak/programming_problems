# http://codeforces.com/problemset/problem/119/A 

import sys

def lcd(a, b):
	if a == b:
		return a
	elif a > b:
		if not a % b:
			return b
		else:
			return lcd(a % b, b)
	else:
		return lcd(b, a)		
		

with open('input.txt', 'r') as f:
	a, b, n = tuple(map(int, f.readline().split()))
	
print(a,b,n)
	
while True:
	if n == 0:
		print(1)
		break
		
	n1 = lcd(n,a)
	if n1 > n:
		print(1)
		break
	else:
		n = n - n1

	if n == 0:
		print(0)
		break
				
	n2 = lcd(n, b)
	if n2 > n:
		print(0)
		break
	else:
		n = n - n2
		
		
