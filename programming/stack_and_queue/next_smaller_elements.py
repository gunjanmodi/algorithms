"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(array):
    stack = []
    result = []
    for i in range(len(array)):
        while stack and array[i] < stack[-1]:
            stack.pop()
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(array[i])
    # result.reverse()
    return result


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([2, 3, 4, 5, 1]))
print(main([4, 8, 5, 2, 25]))
