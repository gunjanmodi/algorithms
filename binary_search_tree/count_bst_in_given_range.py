class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def count_bst_in_given_range(root, low, high):
    result = []
    traversal(root, low, high, result)
    return len(result)
    
def traversal(root, low, high, result):
    if root is None:
        return
    if low <= root.data <= high:
        result.append(root.data)
    if root.data >= low:
        traversal(root.left, low, high, result)
    if root.data <= high:
        traversal(root.right, low, high, result)


root = Node(4)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(2)
print(count_bst_in_given_range(root, 2, 4))