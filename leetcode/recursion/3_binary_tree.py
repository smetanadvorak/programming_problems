# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return
# the subtree rooted with that node. If such a node does not exist,
# return null.
#
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []

from ListsAndTrees import BST

class Solution:
    def searchBST(self, root, val):
        if root == None:
            return None
        else:
            if root.val == val:
                return root
            else:
                if val < root.val:
                    result = self.searchBST(root.left, val)
                if val > root.val:
                    result = self.searchBST(root.right, val)
                return result


S = Solution()

# Input 1
l = [3,1,2,4,5]
T = BST(l)

print('\nBST:')
print(T)

out=S.searchBST(T.root,1)
print('\nResult on request', 1)
print(out)

# Input 2
l = [4,2,7,1,3]
T = BST(l)

print('\nBST:')
print(T)

out=S.searchBST(T.root,2)
print('\nResult on request', 2)
print(out)

# Input 3
l = [4,2,7,1,3]
T = BST(l)

print('\nBST:')
print(out)

out=S.searchBST(T.root,5)
print('\nResult on request', 5)
print(out)
