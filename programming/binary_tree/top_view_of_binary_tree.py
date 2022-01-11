from collections import deque

def top_view(root):
    d = {}
    queue = deque()
    queue.append((0, root))
    while len(queue) > 0:
        count, node = queue.popleft()
        if count not in d:
            d[count] = node.data
        if node.left:
            queue.append((count - 1, node.left))
        if node.right:
            queue.append((count + 1, node.right))
    result = [item[1] for item in sorted(d.items())]
    return result


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8) 
print(top_view(root))
        