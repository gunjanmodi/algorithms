"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(expression):
    stack = []
    for i in range(len(expression)):
        token = expression[i]
        if token != ')':
            stack.append(token)
        else:
            if len(stack) == 1 and stack[-1] == '(':
                return True
            item = stack.pop()
            while item != '(':
                item = stack.pop()




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("((a+b))"))
# print(main("(a+(b)/c)"))
print(main("(a+b*(c-d))"))