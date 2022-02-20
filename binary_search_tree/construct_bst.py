class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.left.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                current_node = current_node.left
            elif value > current_node.right.value:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                current_node = current_node.value
        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def remove(self, value, parent=None):
        # Find the node
        current_node = self
        node_to_remove = None
        while current_node is not None:
            if value == current_node.value:
                node_to_remove = current_node
            elif value < current_node.value:
                parent = current_node
                current_node = current_node.left
            else:
                parent = current_node
                current_node = current_node.right
        # node does not exist
        if node_to_remove is None:
            return False
        elif node_to_remove.left is None and node_to_remove.right is None:
            current_node.value = current_node.right.get_min_value()
            current_node.right.remove(current_node.value, current_node)
        # node is root
        elif parent is None:
            pass

    def get_min_value(self):
        current_node = self
        while current_node is not None:
            current_node = current_node.left
        return current_node.value





