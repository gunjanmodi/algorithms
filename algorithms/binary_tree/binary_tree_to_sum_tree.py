class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def to_sum_tree(node):
    if node is None:
        return 0
        
    old_data = node.data
    
    node.data = to_sum_tree(node.left) + to_sum_tree(node.right)
    
    return node.data + old_data


root = Node(7)
root.left = Node(9)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(8) 
root.right.left = Node(6)
root.left.left.left = Node(10)
root.left.left.right = Node(9)

print(to_sum_tree(root))