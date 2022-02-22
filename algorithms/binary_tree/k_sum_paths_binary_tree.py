class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def k_sum_paths(root, k):
    path = []
    result = []
    helper(root, path, k, result)
    return result

def helper(root, path, k, result):
    if root is None:
        return
    
    path.append(root.data)

    helper(root.left, path, k, result)
    helper(root.right, path, k, result)

    total = 0
    for i in reversed(range(len(path))):
        total += path[i]
        if total == k:
            result.append(path[i:])
    path.pop()


root = Node(1)
root.left = Node(3)
root.right = Node(-1)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right.right = Node(6)
print(k_sum_paths(root, 5))