class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_tree(inorder, preorder):
    if inorder:
        i = inorder.index(preorder.pop(0))
        root = Node(inorder[i])
        root.left = build_tree(inorder[0:i], preorder)
        root.right = build_tree(inorder[i+1:], preorder)
        return root

def build_tree_1(inorder, preorder):
    preorder.reverse()
    inorder_dict = {}
    for i, num in enumerate(inorder):
        inorder_dict[num] = i

    def helper(start, end):
        if start > end:
            return
        value = preorder.pop()
        i = inorder_dict[value]
        root = Node(value)
        root.left = helper(preorder, start, i - 1)
        root.right = helper(preorder, i + 1, end)
    return helper(0, len(preorder) - 1)


print(build_tree([3, 1, 4, 0, 5, 2], [0, 1, 3, 4, 2, 5]))        