from Heap import Heap

def heapSort(arr):
    heap = Heap(arr)
    sorted = []
    for i in range(len(heap.heap)):
        sorted.append(heap.heap[0])
        heap.heap[0] = -heap.heap[0] # Fill the end with values that will definitely stay there
        heap.heapify()
    return sorted

input = list(range(16))
print('Input: ', input)
print('Sorted: ', heapSort(input))
