import unittest

def nodeDepths1(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths1(node.left, depth+1) + nodeDepths1(node.right, depth+1)

def nodeDepths(root):
    sum_of_depths = 0
    stack = [{'node': root, 'depth': 0} ]
    while len(stack) > 0:
        node_info = stack.pop()
        node, depth = node_info['node'], node_info['depth']
        if node is None:
            continue
        sum_of_depths += depth
        stack.append({'node': node.left, 'depth': depth + 1})
        stack.append({'node': node.right, 'depth': depth + 1})
    return sum_of_depths

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
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)

if __name__ == '__main__':
    unittest.main()