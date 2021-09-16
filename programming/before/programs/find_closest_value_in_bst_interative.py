class BST:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                current_node = current_node.right
        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def findClosesValue(self, target):
        current_node = self
        difference = float("inf")
        possible_value = None
        while current_node is not None:
            current_difference = abs(current_node.value - target)
            if current_difference < difference:
                difference = current_difference
                possible_value = current_node.value
            if target < current_node.value:
                current_node = current_node.left
            elif target > current_node.value:
                current_node = current_node.right
        return possible_value

    def remove(self, value, parent = None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.right.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.right = current_node.right.right
                        current_node.left =  current_node.left.left
                    else:
                        pass
                elif parent.left == current_node:
                    parent.left = current_node.left if current_node.left is not None else current_node.right
                elif parent.right == current_node:
                    parent.right = current_node.left if current_node.left is not None else current_node.right
                break
                
        return self

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    tree = BST(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(13)
    tree.insert(22)
    tree.insert(14)
    tree.insert(3)
    tree.insert(4)

    print("--- CONTAINS ---")
    print(tree.contains(15))

    print(tree.findClosesValue(12))
    # tree.remove(5)