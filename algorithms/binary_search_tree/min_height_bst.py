import unittest

# ------- SOLUTION 1 -------- #
# O(nlog(n)) time | O(n) spce

"""
def minHeightBst(array):
    return construct_min_height_bst(array, None, 0, len(array) - 1)

def construct_min_height_bst(array, bst, start_idx, end_idx):
    if end_idx < start_idx:
        return
    mid_idx = (start_idx + end_idx) // 2
    value_to_insert = array[mid_idx]
    if bst is None:
        bst = BST(value_to_insert)
    else:
        bst.insert(value_to_insert)
    construct_min_height_bst(array, bst, start_idx, mid_idx - 1)
    construct_min_height_bst(array, bst, mid_idx + 1, end_idx)
    return bst
"""

# -------- Solution 2 -------
# O(n) time | O(n) space
"""
def minHeightBst(array):
    return construct_min_height_bst(array, None, 0, len(array) - 1)

def construct_min_height_bst(array, bst, start_idx, end_idx):
    if end_idx < start_idx:
        return
    mid_idx = (start_idx + end_idx) // 2
    new_bst = BST(array[mid_idx])
    if bst is None:
        bst = new_bst
    else:
        if new_bst.value < bst.value:
            bst.left = new_bst
            bst = bst.left
        else:
            bst.right = new_bst
            bst = bst.right
        
    construct_min_height_bst(array, bst, start_idx, mid_idx - 1)
    construct_min_height_bst(array, bst, mid_idx + 1, end_idx)
    return bst
"""

# ------ Solution 3 More cleaner code -------
# O(n) time | O(n) space

def minHeightBst(array):
    return construct_min_height_bst(array, 0, len(array) - 1)

def construct_min_height_bst(array, start_idx, end_idx):
    if end_idx < start_idx:
        return
    mid_idx = (start_idx + end_idx) // 2
    bst = BST(array[mid_idx])
        
    bst.left = construct_min_height_bst(array, start_idx, mid_idx - 1)
    bst.right = construct_min_height_bst(array, mid_idx + 1, end_idx)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)

def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
        tree = minHeightBst(array)

        self.assertTrue(validateBst(tree))
        self.assertEqual(getTreeHeight(tree), 4)

        inOrder = inOrderTraverse(tree, [])
        
        self.assertEqual(inOrder, [1, 2, 5, 7, 10, 13, 14, 15, 22])


if __name__ == '__main__':
    unittest.main()
