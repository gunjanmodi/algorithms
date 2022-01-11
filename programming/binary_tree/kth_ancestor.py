from typing import AnyStr


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def kth_ancestor(root, node, k):
    path = []
    result = []
    def helper(root, parent, path, k, result):
        if root is None:
            return
        if parent != -1:
            path.append(parent)
        if root.data == node:
            node_path = path[:]
            answer = -1
            while k >= 1:
                answer = node_path.pop()
                k -= 1
            result.append(answer)
        helper(root.left, root.data, path, k, result)
        helper(root.right, root.data, path, k, result)
        if parent != -1:
            path.pop()

    helper(root, -1, path, k, result)
    return result[-1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
print(kth_ancestor(root, 7 , 2))


# root = Node(7)
# root.left = Node(9)
# root.right = Node(5)
# print(kth_ancestor(root, 9, 5))