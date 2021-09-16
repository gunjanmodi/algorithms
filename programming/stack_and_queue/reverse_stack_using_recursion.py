"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(stack):
    new_stack = []
    stack_helper(stack, new_stack)
    return new_stack


def stack_helper(stack, new_stack):
    if len(stack) == 0:
        return
    top = stack.pop()
    new_stack.append(top)
    stack_helper(stack, new_stack)

# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([5, 9, 4, 7, 6]))