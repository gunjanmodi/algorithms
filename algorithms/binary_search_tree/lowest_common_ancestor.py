class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def lca_bst(root, n1, n2):
    if root is None:
        return
    
    if root.data < n1 and root.data < n2:
        return lca_bst(root.right, n1, n2)
    elif root.data > n1 and root.data > n2:
        return lca_bst(root.left, n1, n2)
    else:
        return root

root = Node(4)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(2)
print(lca_bst(root, 3, 1).data)