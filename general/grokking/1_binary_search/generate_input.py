import sys

if len(sys.argv) > 1:
	arrlen = int(sys.argv[1])
else:
	print('Please, specify the number of array entries.\n')
	arrlen = int(input())
	
print(arrlen)

outfile = open('database.txt', 'w')
for i in range(arrlen-1):
	outfile.writelines(str(i)+'\n')

outfile.close()