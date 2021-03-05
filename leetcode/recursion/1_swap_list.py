# Given a linked list, swap every two adjacent nodes and return its head.
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

from ListsAndTrees import LinkedList

class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        elif not head.next:
            return head
        else:
            print(head.val, head.next.val)
            dummy = head.next # The element to become the first one
            if head.next.next: # Run on next pair first
                head.next = self.swapPairs(head.next.next)
            else:
                head.next = None
            dummy.next = head # Now make previous head to be second
            return dummy  # Return new head


S = Solution()

# Input 1
l = [1,2,3,4]
L = LinkedList()
L.insert(l)
print('\nInput:')
print(L)

L.head = S.swapPairs(L.head)

print('\nOutput:')
print(L)


# Input 2
l = []
L = LinkedList()
L.insert(l)
print('\nInput:')
print(L)

L.head = S.swapPairs(L.head)

print('\nOutput:')
print(L)
