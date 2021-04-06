# Prefix trees or tries are used to store such data elements as strings, in a way
# that cheking if the string is in the tree takes linear time, at worst.
# Adding a new string is also a linear operation .
# Data elements, thus, are contained in the leafs of the tree (but this can be
# omitted during implementation), other nodes being roadsigns in their search. 

class Trie:
    def __init__(self, value=''):
        self.value = value
        self.children = {}


    def add_child(self, arrow, node):
        self.children[arrow] = node
        self.children[arrow].value = arrow

    def get_child(self, arrow):
        return self.children[arrow]

    def get_arrows(self):
        return self.children.keys()

    def get_children(self):
        return [self.get_child(arrow) for arrow in self.get_arrows()]

    def insert(self, key):
        current_node = self
        for char in key:
            if not char in current_node.get_arrows():
                current_node.add_child(char, Trie(char))
            current_node = current_node.get_child(char)

    def insert_recursive(self, key):
        if len(key) == 0:
            return
        if key[0] in self.get_arrows():
            next_node = self.children[key[0]]
        else:
            next_node = Trie()
            self.add_child(key[0], next_node)
        next_node.insert(key[1:])


    def find(self, key):
        if len(key) == 0:
            return True
        if not key[0] in self.get_arrows():
            return False
        self.children[key[0]].find(key[1:])

    def print(self):
        next_nodes = [self]
        while next_nodes:
            curr_nodes = next_nodes
            next_nodes = []
            for node in curr_nodes:
                print(node.value, end='')
                next_nodes += node.get_children()
            print()


if __name__ == '__main__':
    trie = Trie()
    trie.insert('abc')
    trie.insert('abd')
    trie.insert('ay')
    trie.insert('aaaaa')
    trie.print()
