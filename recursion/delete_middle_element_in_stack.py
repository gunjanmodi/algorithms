"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from data_structures.stack import Stack
import math
# Time: O() | Space: O()
def delete_middle_in_stack():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    middle_index = stack.get_middle_index()
    delete_middle_helper(stack, middle_index)


def deleteMid(self, s, sizeOfStack):
    middle_index = math.ceil(sizeOfStack // 2)
    
    def delete_mid_helper(stack, middle_index):
        if middle_index == 0:
            stack.pop()
            return
        top = stack.pop()
        delete_mid_helper(stack, middle_index - 1)
        stack.append(top)
        
    delete_mid_helper(s, middle_index)
    return s


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(delete_middle_in_stack())