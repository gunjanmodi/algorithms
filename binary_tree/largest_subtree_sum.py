class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def largest_subtree_sum(root):
    max_sum = float('-inf')

    def helper(node, max_sum):
        if node is None:
            return 0
        left_sum = helper(node.left, max_sum)
        right_sum = helper(node.right, max_sum)

        current_sum = node.data + left_sum + right_sum
        max_sum =  max(current_sum, max_sum)
        return current_sum
    
    return helper(root, max_sum)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(largest_subtree_sum(root))


root = Node(1)
root.left = Node(-2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(-6)
root.right.right = Node(2)
print(largest_subtree_sum(root))