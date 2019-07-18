class Node:
	def __init__(self, key):
		self.val = key
		self.right = None
		self.left = None


def haspath(node, path):
	path = path + [node.val]
	if node is None:
		return 0
	if node.left is None and node.right is None:
		print(path)

	if node.left is not None:
		haspath(node.left, path)
	if node.right is not None:
		haspath(node.right, path)


root = Node(6)

root.left = Node(3)
root.right = Node(5)

root.left.left = Node(1)
root.left.right = Node(5)

root.right.right = Node(4)

root.left.right.left = Node(7)
root.left.right.right = Node(4)

haspath(root, path=[])
