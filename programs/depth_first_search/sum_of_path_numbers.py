class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  return find_sum_of_path_numbers_helper(root, 0)

def find_sum_of_path_numbers_helper(current_node, path_sum):
  if current_node is None:
    return 0
  path_sum = 10 * path_sum + current_node.val
  if current_node.left is None and current_node.right is None:
    return path_sum
  return find_sum_of_path_numbers_helper(current_node.left, path_sum) + find_sum_of_path_numbers_helper(current_node.right, path_sum)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
