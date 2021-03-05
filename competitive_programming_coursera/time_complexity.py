import sys, time

if len(sys.argv) > 1:
	l,m,n = tuple(map(int,sys.argv[1:4]))
else: 
	l,m,n = (100,100,1000)
	
start_time = time.time()
for i in range(l):
	for j in range(m):
		for k in range(n):
			a = i+j+k

print('Time complexity O(lmn): %d' % (l*m*n))
print('Execution time: %s seconds' % (time.time() - start_time))

