class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def search(root, val):
    if root is None:
        return
    if val == root.data:
        return root
    elif val < root.data:
        return search(root.left, val)
    else:
        return search(root.right, val)


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(search(root, 2))