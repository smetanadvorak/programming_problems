import sys

with open('input.txt', 'r') as f:
	k, m, d = tuple(map(int, f.readline().split()))

print('per day: ', k, 'books had: ', m, 'day: ', d)

needs_to_read = 1
days_happy = 0
while True:
	# Go to the library
	if d > 0 and d < 6: # If it is open, take k new books
		m = m + k
	
	if m >= need_to_read:	
		# Read the books
		m = m - need_to_read
	
		# Increment books number and days count
		need_to_read += 1
		days_happy += 1
		d = (d+1)%7
	else: 
		break
	
print(days_happy)
	