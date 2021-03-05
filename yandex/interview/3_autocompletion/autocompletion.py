
class Node:
	def __init__(self, value):
		self.value = value
		self.children = {}


class PrefixTree:
	def __init__(self):
		self.root = Node('')

	def find(self, query):
		current_node = self.root
		for ch in query:
			if ch in current_node.children.keys():
				current_node = current_node.children[ch]
			else:
				return None
		return True

	def suggest_single_autocorrection(self, query):
		current_node = self.root
		for ch in query:
			if ch in current_node.children.keys():
				current_node = current_node.children[ch]
			else:
				return None

		suggestion = query
		while len(current_node.children):
			if len(current_node.children) > 1:
				return None
			else:
				next_character = list(current_node.children.keys())[0]
				suggestion += next_character
				current_node = current_node.children[next_character]

		return suggestion


	def add(self, entry):
		current_node = self.root
		for ch in entry:
			if not ch in current_node.children.keys():
				current_node.children[ch] = Node(ch)
			current_node = current_node.children[ch]


with open('input2.txt', 'r') as f:
	n = int(f.readline())
	text = f.readline()
	words = text.split()


trie = PrefixTree()

keystrokes = 0
for word in words:
	print('Current word:', word)
	autocompletion_used = False
	for c in range(len(word)):
		keystrokes   += 1
		print(word[:c+1], keystrokes)
		suggestion = trie.suggest_single_autocorrection(word[:c+1])
		if suggestion == word:
			print('Autocompleted:', suggestion)
			autocompletion_used = True
			break

	if not autocompletion_used:
		print('Added:', word)
		trie.add(word)

print(keystrokes)
