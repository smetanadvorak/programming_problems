# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.
#
# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
#
#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data is None:
            self.data = value
            return

        if value >= self.data:
            if self.right is None:
                self.right = Node(None)
            self.right.insert(value)
        else:
            if self.left is None:
                self.left = Node(None)
            self.left.insert(value)
        return self


    def PrintTree(self, mode='inorder'):
        if mode == 'inorder':
            if not self.left is None:
                self.left.PrintTree(mode)
            if not self.data is None:
                print(self.data)
            if not self.right is None:
                self.right.PrintTree(mode)

        elif mode == 'preorder':
            if not self.data is None:
                print(self.data)
            if not self.left is None:
                self.left.PrintTree(mode)
            if not self.right is None:
                self.right.PrintTree(mode)

        elif mode == 'postorder':
            if not self.left is None:
                self.left.PrintTree(mode)
            if not self.right is None:
                self.right.PrintTree(mode)
            if not self.data is None:
                print(self.data)

def restoreTreeFromPostorder(elements):
    if len(elements) == 0:
        return None
    if len(elements) == 1:
        return Node(elements[0])

    root = Node(elements[-1])
    right_subtree = [elem for elem in elements if elem > root.data]
    left_subtree = [elem for elem in elements if elem < root.data]
    root.left = restoreTreeFromPostorder(left_subtree)
    root.right = restoreTreeFromPostorder(right_subtree)
    return root






T = Node(None)
elements = [5,3,7,2,4,8]
for e in elements:
    T.insert(e)

print('Inorder:')
T.PrintTree('inorder')
print('Preorder:')
T.PrintTree('preorder')
print('Postorder:')
T.PrintTree('postorder')

post = [2, 4, 3, 8, 7, 5]
R = restoreTreeFromPostorder(post)
R.PrintTree('postorder')
