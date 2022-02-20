class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


class Solution:
    def boundary_traversal(self, root):
        result = []
        result.append(root.data)
        result = self.left_boundary_traversal(root, result)
        result = self.leaf_node_traversal(root, result)
        result = self.right_boundary_traversal(root, result)
        return result
            
            
    def left_boundary_traversal(self, node, result):
        current = node.left
        while current is not None:
            if not self._is_leaf_node(current):
                result.append(current.data)

            if current.left:
                current = current.left
            else:
                current = current.right
        return result


    def right_boundary_traversal(self, node, result):
        current = node.right
        temp_result = []
        while current is not None:
            if not self._is_leaf_node(current):
                temp_result.append(current.data)
            if current.right:
                current = current.right
            else:
                current = current.left

        while len(temp_result) > 0:
            result.append(temp_result.pop())
        return result


    def leaf_node_traversal(self, node, result):
        self._pre_order_traversal(node, result)
        return result
        
    def _pre_order_traversal(self, node, result):
        if node is None:
            return
        if self._is_leaf_node(node):
            result.append(node.data)
            return
        if node.left:
            self._pre_order_traversal(node.left, result)
        if node.right:
            self._pre_order_traversal(node.right, result)

    def _is_leaf_node(self, node):
        return node.left is None and node.right is None

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.left.right = Node(4)
    root.left.left.right.left = Node(5)
    root.left.left.right.right = Node(6)
    root.right.right = Node(8)
    root.right.right.left = Node(9)
    root.right.right.left.left = Node(10)
    root.right.right.left.right = Node(11)
    s = Solution()
    print(s.boundary_traversal(root))
