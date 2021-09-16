import unittest

def max_path_sum(tree):
    _, max_sum = find_max_sum(tree)
    return max_sum

def find_max_sum(tree):
    if tree is None:
        return (0, float('-inf'))
    left_max_sum_as_branch, left_max_sum = find_max_sum(tree.left)
    right_max_sum_as_branch, right_max_sum = find_max_sum(tree.right)
    max_child_sum_as_branch = max(left_max_sum_as_branch, right_max_sum_as_branch)

    value = tree.value
    max_sum_as_branch = max(max_child_sum_as_branch + value, value)
    max_sum_as_root = max(left_max_sum_as_branch + value + right_max_sum_as_branch, max_sum_as_branch)
    max_path_sum = max(left_max_sum, right_max_sum, max_sum_as_root)
    return (max_sum_as_branch, max_path_sum)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(max_path_sum(test), 18)

class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

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

if __name__ == '__main__':
    unittest.main()
