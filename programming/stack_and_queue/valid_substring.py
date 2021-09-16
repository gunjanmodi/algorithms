"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(string):
    stack = [-1]
    count = 0
    for i, token in enumerate(string):
        if token == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()

            if len(stack) != 0:
                count = max(count, i - stack[len(stack) - 1])
            else:
                stack.append(i)
    return count


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("))()(()"))
print(main("(()("))
print(main("()(())("))