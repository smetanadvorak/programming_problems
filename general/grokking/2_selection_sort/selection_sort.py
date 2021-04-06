
def selection_sort(arr):
	for i in range(len(arr)):
		smallest_ind = i + find_smallest(arr[i:])
		dummy = arr[i]
		arr[i] = arr[smallest_ind]
		arr[smallest_ind] = dummy
	return arr

def find_smallest(arr):
	smallest_ind = 0
	smallest_val = arr[smallest_ind]

	for i in range(1, len(arr)):
		if arr[i] < smallest_val:
			smallest_ind = i
			smallest_val = arr[i]
			
	return smallest_ind


#arr = [152, 111, 4, 10, 66, 213, 95, 24]
arr = ['ab','ba','abc', 'bac', 'bacd', 'b', 'a']
print(selection_sort(arr))

