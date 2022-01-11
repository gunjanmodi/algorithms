class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_isomorphic(r1, r2):
    if r1 is None and r2 is None:
        return True # If both nodes are NULL, trees are isomorphic
    if r1 is None or r2 is None:
        return False # If one node is NULL and one node is having data then trees are not isomorphic
    if r1.data != r2.data:
        return False # If data of root node is different then trees are not isomorphic
    return is_isomorphic(r1.left, r2.right) and is_isomorphic(r1.right, r2.left) or is_isomorphic(r1.left, r2.left) and is_isomorphic(r1.right, r2.right)
