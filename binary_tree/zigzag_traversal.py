def zigzag_traversal(root):
    result = []
    current_level = [root]
    next_level = []
    ltr = True
    while len(current_level) > 0:
        node = current_level.pop()
        result.append(node.data)
        if ltr:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        if len(current_level) == 0:
            ltr = not ltr
            current_level, next_level = next_level, current_level
    return result
        


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

print(zigzag_traversal(root))
        