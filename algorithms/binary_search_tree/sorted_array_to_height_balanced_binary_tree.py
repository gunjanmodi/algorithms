class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def sorted_array_to_balanced_BST(nums):
    def dfs(left, right):
        if left > right:
            return None
            
        mid = (left + right) // 2
        root = Node(nums[mid])
        root.left = dfs(left, mid - 1)
        root.right = dfs(mid+1, right)
        return root
    
    return dfs(0, len(nums) - 1)

root = Node(4)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(2)
print(sorted_array_to_balanced_BST([1,2,3,4,8]))