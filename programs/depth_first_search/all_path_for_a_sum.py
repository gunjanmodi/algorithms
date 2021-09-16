class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_paths(root, required_sum):
    all_paths = []
    current_paths = []
    find_path_helper(root, required_sum, current_paths, all_paths)
    return all_paths

def find_path_helper(current_node, required_sum, current_paths, all_paths):
    if current_node is None:
        return
    current_paths.append(current_node.val)
    if current_node is None:
        return
    if current_node.val == required_sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_paths))
    else:
        find_path_helper(current_node.left, required_sum - current_node.val, current_paths, all_paths)
        find_path_helper(current_node.right, required_sum - current_node.val, current_paths, all_paths)
    del current_paths[-1]




def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))

main()