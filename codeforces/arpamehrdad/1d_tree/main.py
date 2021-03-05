import sys

tree = {}

class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
	
	def add(self, node):
		self.children.append(node)


def check_palindrome(str):
	hist = [0 for i in range(22)] #The problem considers only letters from a to v, hence 22 characters
	# To be a palindrome (after shuffling) the string should contain a pair number of each letter, 
	# but it is allowed to have one with impair number of appearances (goes to the middle of the palindrome)
	for c in str:
		hist[ord(c) - ord(a)] = (hist[ord(c)-ord(a)]+1) % 2
	
	if sum(hist) <= 1:
		return True
	else:
		return False

with open('input.txt', 'r') as f:
	n = int(f.readline())
	tree[1] = Node('')
	for i in range(2,n+1):
		line = f.readline().split()
		p, letter = (int(line[0]), line[1])
		
		tree[p].add(Node(letter))
		tree[i] = tree[p].children[-1]
		

		
		