class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def longest_common_ancestor(root, n1, n2):
        parent_dict = {}
        dfs_generate_parents(root, '-1', parent_dict)
        
        stack1, stack2 = [], []
        while n1 != '-1':
            stack1.append(n1)
            n1 = parent_dict[n1]
            
        while n2 != '-1':
            stack2.append(n2)
            n2 = parent_dict[n2]
        
        lca = root.val
        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            lca = stack1.pop()
            stack2.pop()
            
        return Node(lca).val
    
        
def dfs_generate_parents(root, parent, parent_dict):
    if root is None:
        return
    parent_dict[root.val] = parent
    dfs_generate_parents(root.left, root.val, parent_dict)
    dfs_generate_parents(root.right, root.val, parent_dict)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(longest_common_ancestor(root, 6, 7))


root = Node(7)
root.left = Node(9)
root.right = Node(5)
print(longest_common_ancestor(root, 9, 5))