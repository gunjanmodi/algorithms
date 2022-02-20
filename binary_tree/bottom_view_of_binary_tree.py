from collections import deque

def bottom_view(root):
    queue = deque()
    other_queue = deque()
    queue.append((0, root))
    while len(queue) > 0:
        count, node = queue.popleft()
        other_queue.append((count, node.data))
        if node.left:
            queue.append((count - 1, node.left))
        if node.right:
            queue.append((count + 1, node.right))
    
    count_ref = {}
    while len(other_queue) > 0:
        count, node = other_queue.pop()
        if count not in count_ref:
            count_ref[count] = node
    return [item[1] for item in sorted(count_ref.items())]


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)
# 
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3) 
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(bottom_view(root))
        