from typing import List


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def bst_from_preorder(preorder):
    if not preorder:
        return None

    root = Node(preorder[0])
    i = 1

    while i<len(preorder) and  preorder[i] < root.val:
        i+=1
    
    root.left = bst_from_preorder(preorder[1:i])
    root.right = bst_from_preorder(preorder[i:])
    return root

def bst_from_preorder_improved(preorder):

    def bst_helper(preorder, left, right):
        if left >= right:
            return

        root = Node(preorder[left])
        
        i = left + 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
            
        root.left = bst_helper(preorder, left + 1, i)
        root.right = bst_helper(preorder, i, right)
        

        return root

    if not preorder:
        return
    return bst_helper(preorder, 0, len(preorder))


def bstFromPreorderStack(self, preorder: List[int]) -> Node:
    root = Node(preorder[0])
    stack = [root]
    for value in preorder[1:]:
        if value < stack[-1].val:
            stack[-1].left = Node(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = Node(value)
            stack.append(last.right)
    return root



