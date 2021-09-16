import unittest

def allKindsOfNodeDepths(root):
    node_counts = {}
    add_node_counts(root, node_counts)
    node_depths = {}
    add_node_depths(root, node_depths, node_counts)
    return sum_all_node_depths(root, node_depths)

def sum_all_node_depths(node, node_depths):
    if node is None:
        return 0
    return sum_all_node_depths(node.left, node_depths) + sum_all_node_depths(node.right, node_depths) + node_depths[node]

def add_node_depths(node, node_depths, node_counts):
    node_depths[node] = 0
    if node.left is not None:
        add_node_depths(node.left, node_depths, node_counts)
        node_depths[node] += node_depths[node.left] + node_counts[node.left]
    if node.right is not None:
        add_node_depths(node.right, node_depths, node_counts)
        node_depths[node] += node_depths[node.right] + node_counts[node.right]

def add_node_counts(node, node_counts):
    node_counts[node] = 1
    if node.left is not None:
        add_node_counts(node.left, node_counts)
        node_counts[node] += node_counts[node.left]
    if node.right is not None:
        add_node_counts(node.right, node_counts)
        node_counts[node] += node_counts[node.right]


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = allKindsOfNodeDepths(root)
        self.assertEqual(actual, 26)

if __name__ == '__main__':
    unittest.main()