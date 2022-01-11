import collections

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def sum_of_longest_root_to_leaf_path(root):
    running_sum = 0
    return helper(root, running_sum, 0)[0]
    
    
def helper(root, running_sum, depth):
    if root is None:
        return running_sum, depth

    running_sum += root.data
    depth += 1

    left_sum, left_depth = helper(root.left, running_sum, depth)
    right_sum, right_depth = helper(root.right, running_sum, depth)
    
    if left_depth > right_depth:
        return left_sum, left_depth
    elif left_depth < right_depth:
        return right_sum, right_depth
    else:
        return max(left_sum, right_sum), left_depth
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(sum_of_longest_root_to_leaf_path(root))