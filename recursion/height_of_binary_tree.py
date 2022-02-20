"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def height(node):
    if node is None:
        return
    return 1 + max(height(node.left), height(node.right))


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
class BT:
    def __init__(self):
        self.left = None
        self.right = None

        
node = BT()
print(height(node))