import unittest

def number_of_tree_topologies(n):
    if n == 0:
        return 1
    number_of_trees = 0
    for left_tree_size in range(n + 1):
        left_subtree_size =  number_of_tree_topologies(left_tree_size)
        right_subtree_size = number_of_tree_topologies(n - 1 - left_tree_size)
        number_of_trees += left_subtree_size * right_subtree_size
    return number_of_trees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(number_of_tree_topologies(3), 5)


if __name__ == '__main__':
    unittest.main()