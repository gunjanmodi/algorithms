"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from data_structures.stack import Stack
# Time: O() | Space: O()
def sort_stack():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    sort_stack_helper(stack)
    print(stack.array)


def sort_stack_helper(stack):
    if stack.length() == 0:
        return
    last_element = stack.pop()
    sort_stack_helper(stack)
    insert(stack, last_element)


def insert(stack, element):
    if stack.length() == 0 or stack.top() <= element:
        stack.push(element)
        return
    top = stack.pop()
    insert(stack, element)
    stack.push(top)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print(sort_stack())
sort_stack()