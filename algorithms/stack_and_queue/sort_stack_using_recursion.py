"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(n^2) | Space: O(n)
def main(stack):
    sort_helper(stack)
    return stack


def sort_helper(stack):
    if len(stack) == 0:
        return
    top = stack.pop()
    sort_helper(stack)
    sorted_insert(stack, top)


def sorted_insert(stack, element):
    if len(stack) == 0 or stack[-1] < element:
        stack.append(element)
        return
    else:
        top = stack.pop()
        sorted_insert(stack, element)
        stack.append(top)

# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([5, 9, 4, 7, 6]))
