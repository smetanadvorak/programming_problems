class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def __str__(self):
        s = []
        head = self.head
        while head:
            s.append(head.val)
            head = head.next
        return str(s)

    def insert(self, val):
        if isinstance(val, list):
            for v in reversed(val):
                self.insert(v)
        else:
            new_node = ListNode(val, self.head)
            self.head = new_node


class BT_node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = []
        def helper(root):
            if root:
                s.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(self)
        return str(s)

class BST:
    def __init__(self, keys=[]):
        if len(keys):
            self.root = BT_node(keys[0])
            for k in keys[1:]:
                self.insert(self.root, k)
        else:
            self.root = None


    def insert(self, root, val):
        if val < root.val:
            if root.left:
                self.insert(root.left, val)
            else:
                root.left = BT_node(val)
        else:
            if root.right:
                self.insert(root.right, val)
            else:
                root.right = BT_node(val)

    def __str__(self):
        s = []
        def helper(root):
            if root:
                s.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(self.root)
        return str(s)
