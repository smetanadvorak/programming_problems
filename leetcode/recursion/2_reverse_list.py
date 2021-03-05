# Given the head of a singly linked list, reverse the list,
# and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

from ListsAndTrees import LinkedList

class Solution:
    def fetchElement(self, head, depth = float('inf')):
        i = 0
        dummy = head
        while dummy.next and i < depth:
            i += 1
            dummy = dummy.next
        return dummy, i

    def helper(self, head, depth=float('inf')):
        if depth==0:
            head.next = None # Cut the last element
            return head
        dummy = head
        head, depth = self.fetchElement(head, depth)
        head.next = self.helper(dummy, depth-1)
        return head

    def reverseList(self, head):
        if not head:
            return head
        if head.next is None:
            return head
        return self.helper(head)

S = Solution()

#Input 1:
l = [1,2,3,4,5]
L = LinkedList()
L.insert(l)

print('\nInput:')
print(L)
L.head = S.reverseList(L.head)
print('\nAfter:')
print(L)


#Input 2:
l = [1,2]
L = LinkedList()
print(L)

print('\nInput:')
print(L)
L.head = S.reverseList(L.head)
print('\nOutput:')
print(L)

#Input 3:
L = LinkedList()
L.insert(l)

print('\nInput:')
print(L)
L.head = S.reverseList(L.head)
print('\nOutput:')
print(L)
