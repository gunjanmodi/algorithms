def is_balanced(root):
    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)

    return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
     


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

 
root = Node(7)
root.left = Node(9)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(8) 
root.right.left = Node(6)
root.left.left.left = Node(10)
root.left.left.right = Node(9)

print(is_balanced(root))
        