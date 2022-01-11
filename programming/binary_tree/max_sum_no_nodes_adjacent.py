class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_max_sum(root):
    choosen = {}
    helper(root, choosen, -1)
    max_sum = 0
    for key in choosen.keys():
        max_sum += key
    return max_sum
    
def helper(root, choosen, parent):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        if root.data > parent.data:
            if parent in choosen:
                choosen[parent.data] = True
            else:
                choosen[root.data] = True
        else:
            if root in choosen:
                choosen[parent.data] = True
            else:
                choosen[root.data] = True
           

    helper(root.left, choosen, root)
    helper(root.right, choosen, root)
    
    return choosen


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

root = Node(7)
root.left = Node(9)
root.right = Node(5)
print(get_max_sum(root))