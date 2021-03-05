https://codeforces.com/problemset/problem/474/A

symb = "qwertyuiopasdfghjkl;zxcvbnm,./"
keyboard = [[symb[i*10+j] for j in range(10)] for i in range(3)]
index = {keyboard[i][j]:(i,j) for j in range(10) for i in range(3)}

shift = 'R'
input = 's;;upimrrfod;pbr'

output = '';
for letter in input:
	row, col = index[letter]
	
	if shift == 'L':
		col = min(col+1, 9)
	
	if shift == 'R':
		col = max(col-1, 0)	
					
	output += keyboard[row][col]
	
print(output)
	

