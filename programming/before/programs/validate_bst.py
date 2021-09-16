class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def validate_bst_helper(tree, min_tree_value, max_tree_value):
    if tree is None:
        return True

    

def validateBst(tree):
    return validate_bst_helper(tree, float("-inf"), float("inf"))
    
        

        


if __name__ == '__main__':
    tree = BST(10)
    n15 = BST(15)
    n22 = BST(22)
    n500 = BST(500)
    n1500 = BST(1500)
    n10000 = BST(10000)
    n9999 = BST(9999)
    n2200 = BST(2200)
    n50 = BST(50)
    n200 = BST(200)
    n5 = BST(5)
    n5_2 = BST(5)
    n2 = BST(2)
    n1 = BST(1)

    tree.left = n5
    tree.right = n15
    n5.left = n2
    n5.right = n5_2
    n2.left = n1

    n15.right = n22
    n22.right = n500
    n500.left = n50
    n50.right = n200
    n500.right = n1500
    n1500.right = n10000
    n10000.left = n2200
    n10000.right = n9999

    print(validateBst(tree))

