class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def kth_largest_element_in_bst(root, k):
    in_order = []
    in_order_traversal(root, in_order)
    while k > 0:
        result = in_order.pop()
        k -= 1
    return result


def kth_smallest_element_in_bst(root, k):
    in_order = []
    in_order_traversal(root, in_order)
    if k > len(in_order):
        return -1
    return in_order[k - 1]


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
print(kth_largest_element_in_bst(root, 2))
print(kth_smallest_element_in_bst(root, 2))