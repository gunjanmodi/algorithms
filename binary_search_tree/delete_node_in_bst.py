class Node:
    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right


def delete_node(root, key):
    
    def delete_node_helper(root, key):
        if root is None:
            return
        if key < root.val:
            root.left = delete_node_helper(root.left, key)
        elif key > root.val:
            root.right = delete_node_helper(root.right, key)
        elif key == root.val:
            if root.left is None and root.right is None:
                return None
            if root.left is None or root.right is None:
                return root.left if root.left else root.right
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = delete_node_helper(root.right, temp.val)
        return root
    
    return delete_node_helper(root, key)


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(delete_node(root, 4).val)