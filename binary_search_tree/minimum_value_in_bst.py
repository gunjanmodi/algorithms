class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def min_value(root):
    if root.left:
        return min_value(root.left)
    else:
        return root.data
    



root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(min_value(root))