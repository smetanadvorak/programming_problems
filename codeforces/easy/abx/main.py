# Дано целое число 𝑥, найдите 2 целых числа 𝑎 и 𝑏, таких, что:
# 
# 1≤𝑎,𝑏≤𝑥
# 𝑏 делит 𝑎 (𝑎 делится на 𝑏).
# 𝑎⋅𝑏>𝑥.
# 𝑎𝑏<𝑥.

import sys

x = int(sys.argv[1])

def findab(x):
	for a in range(1, x+1):
		b = a
		while b + a <= x:
			b += a
			if a * b > x :
				return a, b
	return -1
				
				
print(findab(x))

# Practically, this function can be better: 
