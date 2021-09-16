"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from data_structures.stack import Stack


# Time: O(n) | Space: O(n)
def reverse_stack():
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack.array)
    reverse_stack_helper(stack)
    print(stack.array)
    return stack


def reverse_stack_helper(stack):
    if stack.length() == 0:
        return
    last = stack.pop()
    reverse_stack_helper(stack)
    insert(stack, last)
    return


def insert(stack, element):
    if stack.length() == 0:
        stack.push(element)
        return
    last = stack.pop()
    insert(stack, element)
    stack.push(last)
    return


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(reverse_stack())
