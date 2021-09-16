class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value == self.value:
            return True

        if value < self.value:
            return self.left.contains(value)
        else:
            return self.right.contains(value)

    def get_min_value(self, value):
        if self.left is None:
            return self.value
        else:
            self.left.getMinValue()

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    tree = BST(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(5)
    tree.insert(1)
    tree.insert(13)
    tree.insert(22)
    tree.insert(14)

    print("--- CONTAINS ---")
    print(tree.contains(1))

