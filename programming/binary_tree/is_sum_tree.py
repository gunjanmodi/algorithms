class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isSumTree(root):
    if root is None or (root.left is None and root.right is None):
        return True
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    if root.data == left_sum + right_sum and isSumTree(root.left) and isSumTree(root.right):
        return True
    else:
        return False
            
def tree_sum(root):
    if root is None:
        return 0
    return root.data + tree_sum(root.left) + tree_sum(root.right)


root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)
print(isSumTree(root))