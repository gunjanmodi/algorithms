import unittest

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# def flatten_binary_tree(root):
#     in_ordered_tree = in_order_traversal(root, [])
#     for i in range(len(in_ordered_tree) - 1):
#         current = in_ordered_tree[i]
#         next_node = in_ordered_tree[i + 1]
#         current.right = next_node
#         next_node.left = current
#     return in_ordered_tree[0]

# def in_order_traversal(tree, array):
#     if tree is not None:
#         in_order_traversal(tree.left, array)
#         array.append(tree)
#         in_order_traversal(tree.right, array)
#     return array



def flattenBinaryTree(tree):
    left_most, _ = flatten_tree(tree)
    return left_most
    

def flatten_tree(node):
    if node.left is None:
        left_most = node
    else:
        left_subtree_left_most, left_subtree_right_most = flatten_tree(node.left)
        connect(left_subtree_right_most, node)
        left_most = left_subtree_left_most

    if node.right is None:
        right_most = node
    else:
        right_subtree_left_most, right_subtree_right_most = flatten_tree(node.right)
        connect(node, right_subtree_left_most)
        right_most = right_subtree_right_most

    return [left_most, right_most]

def connect(left, right):
    left.right = right
    right.left = left

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1).insert([2, 3, 4, 5, 6])
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        leftMostNode = flattenBinaryTree(root)
        leftToRightToLeft = leftMostNode.leftToRightToLeft()
        expected = [4, 2, 7, 5, 8, 1, 6, 3, 3, 6, 1, 8, 5, 7, 2, 4]
        self.assertEqual(leftToRightToLeft, expected)


class BinaryTree(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def leftToRightToLeft(self):
        nodes = []
        current = self
        while current.right is not None:
            nodes.append(current.value)
            current = current.right
        nodes.append(current.value)
        while current is not None:
            nodes.append(current.value)
            current = current.left
        return nodes

if __name__ == '__main__':
    unittest.main()