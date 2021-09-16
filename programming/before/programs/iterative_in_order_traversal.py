import unittest

def iterative_in_order_traversal(tree, callback):
    previous_node = None
    current_node = tree
    while current_node is not None:
        if previous_node is None or current_node.parent == previous_node:
            if current_node.left is not None:
                next_node = current_node.left
            else:
                callback(current_node)
                next_node = current_node.right if current_node.right is not None else current_node.parent
        elif current_node.left == previous_node:
            callback(current_node)
            next_node = current_node.right if current_node.right is not None else current_node.parent
        else:
            next_node = current_node.parent
        previous_node = current_node
        current_node = next_node
    

class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        return str(self.value)


def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, parent=root)
        root.left.left = BinaryTree(4, parent=root.left)
        root.left.left.right = BinaryTree(9, parent=root.left.left)
        root.right = BinaryTree(3, parent=root)
        root.right.left = BinaryTree(6, parent=root.right)
        root.right.right = BinaryTree(7, parent=root.right)

        testArray = []
        actualTestCallback = lambda x: testCallback(testArray, x)
        iterative_in_order_traversal(root, actualTestCallback)
        self.assertEqual(testArray, [4, 9, 2, 1, 6, 3, 7])


if __name__ == '__main__':
    unittest.main()