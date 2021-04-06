#In computer science, a heap is a specialized tree-based data structure which is essentially an almost complete[1] tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C.[2] The node at the "top" of the heap (with no parents) is called the root node.

#The heap is one maximally efficient implementation of an abstract data type called a priority queue, and in fact, priority queues are often referred to as "heaps", regardless of how they may be implemented. In a heap, the highest (or lowest) priority element is always stored at the root. However, a heap is not a sorted structure; it can be regarded as being partially ordered. A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority.

#A common implementation of a heap is the binary heap, in which the tree is a binary tree (see figure).

class Heap:
    def __init__(self, arr = None):
        if arr:
            self.heap = arr
            self.buildHeap()
        else:
            self.heap = []

# ... Therefore, given a node at index i, its children are at indices 2i + 1 and 2i + 2, and its parent is at index floor((i-1)/2). This simple indexing scheme makes it efficient to move "up" or "down" the tree.
    def heapify(self, ind = 0):
        l_child = 2*ind + 1
        r_child = 2*ind + 2
        largest = ind

        if l_child < len(self.heap) and self.heap[largest] < self.heap[l_child]:
            largest = l_child

        if r_child < len(self.heap) and self.heap[largest] < self.heap[r_child]:
            largest = r_child

        if largest != ind:
            self.heap[ind], self.heap[largest] = self.heap[largest], self.heap[ind]
            self.heapify(largest)

    def buildHeap(self):
        for ind in reversed(range(int(len(self.heap)/2))):
            self.heapify(ind)

    def insert(self, value):
        self.heap.append(value)
        self.siftup(len(self.heap)-1)

    def siftup(self, ind):
        parent = int((ind-1)/2)
        if ind and self.heap[parent] < self.heap[ind]:
            self.heap[parent], self.heap[ind] = self.heap[ind], self.heap[parent]
            self.siftup(parent)


    def printHeap(self, ind = 0):
        def printLevel(level, ind=0):
            if ind < len(self.heap):
                if level == 0:
                    print('%d ' % self.heap[ind], end='')
                else:
                    l_child = 2*ind + 1
                    r_child = 2*ind + 2
                    printLevel(level-1, l_child), printLevel(level-1, r_child)

        for l in range(len(self.heap).bit_length()):
            print('Level %d: ' % l, end='')
            printLevel(l)
            print()


if __name__ == "__main__":
    print('Heapification:')
    heap = Heap(list(range(16)))
    heap.printHeap()

    print('Insertion of a new element')
    for i in range(17):
        heap.insert(100 + i)
    heap.printHeap()
