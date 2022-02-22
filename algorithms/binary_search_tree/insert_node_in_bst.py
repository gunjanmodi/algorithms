class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, value):

    def dfs(root, value):
        if value < root.data:
            if root.left:
                dfs(root.left, value)
            else:
                root.left = Node(value)
        elif value > root.data:
            if root.right:
                dfs(root.right, value)
            else:
                root.right = Node(value)
        else:
            return Node(value)

    if root is None:
        return Node(value)
    dfs(root, value)
    return root

root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(insert(root, 5))