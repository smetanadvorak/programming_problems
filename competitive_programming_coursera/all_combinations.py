# Generate all possible strings that are combinations of letters a and b of length n

import sys
	
def all_combinations(alphabet, n):
	if n == 1:
		return [letter for letter in alphabet]
	elif n > 1:
		combs = []
		for letter in alphabet:
			for comb in all_combinations(alphabet, n-1):
				combs.append(letter+comb)
		return combs
	else:
		return ''



if len(sys.argv) > 1:
	n = int(sys.argv[1])
else:
	n = 4
	
alphabet = 'ab'

print(all_combinations(alphabet, n))

