from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def diagonal_traversal(root):
    left_child_exists_queue = deque()
    queue = deque()
    queue.append(root)
    result = []
    while len(queue) > 0:
        node = queue.popleft()
        result.append(node.data)
        if node.right:
            queue.append(node.right)
        if node.left:
            left_child_exists_queue.append(node.left)
        if len(queue) == 0 and len(left_child_exists_queue) > 0:
            queue.append(left_child_exists_queue.popleft())
    return result

if __name__ == '__main__':
    root  = Node(8)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right.left = Node(13)
    print(diagonal_traversal(root))