class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def binary_tree_to_bst(root):
    in_order = []
    in_order_traversal(root)

    in_order.sort()

    return array_to_bst(in_order, root)


def array_to_bst(array, root):
    if root is None:
        return

    array_to_bst(array, root.left)

    num = array.pop(0)
    root = Node(num)

    array_to_bst(array, root.right)

def in_order_traversal(root, result):
    if root is None:
        return
    in_order_traversal(root.left, result)
    result.append(root.data)
    in_order_traversal(root.right, result)

root = Node(4)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(2)
print(binary_tree_to_bst(root))