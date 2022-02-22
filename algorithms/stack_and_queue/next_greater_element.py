"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def circular_main(array):
    result = [-1] * len(array)
    stack = []
    for i in range(2 * len(array)):
        circular_idx = i % len(array)
        current = array[circular_idx]
        while stack and array[stack[-1]] < current:
            top = stack.pop()
            result[top] = current
        stack.append(circular_idx)
    return result


def main(array):
    result = [-1] * len(array)
    stack = []
    for i in range(len(array)):
        current = array[i]
        while stack and array[stack[-1]] < current:
            top = stack.pop()
            result[top] = current
        stack.append(i)
    return result


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 3, 2, 4]))
print(main([6, 8, 0, 1, 3]))
print(main([2, 5, -3, -4, 6, 7, 2]))