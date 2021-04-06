str1 = "fish"
str2 = "fosh"

def find_longest_substring(str1, str2):
	valuetab = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
	bestval = 0
	bestind = 0
	
	for i in range(1, len(str1)+1, 1):
		for j in range(1, len(str2)+1, 1):
			valuetab[i][j] = (str1[i-1] == str2[j-1]) * (valuetab[i-1][j-1] + 1)
			if valuetab[i][j] > bestval:
				bestind = i
				bestval = valuetab[i][j]
	
	substring = str1[bestind-bestval : bestind]
			
	return valuetab, substring
	
	
def find_longest_subsequence(str1, str2):
	valuetab = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
	bestval = 0
	bestind = 0
	
	for i in range(1, len(str1)+1, 1):
		for j in range(1, len(str2)+1, 1):
			valuetab[i][j] = max(valuetab[i][j-1], valuetab[i-1][j], (str1[i-1] == str2[j-1]) * (valuetab[i-1][j-1] + 1))
			
	return valuetab
	
print(find_longest_substring(str1, str2))
print(find_longest_subsequence(str1, str2))