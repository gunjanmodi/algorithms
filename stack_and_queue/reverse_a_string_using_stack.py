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
    stack = Stack()
    for chr in string:
        stack.push(chr)
    reversed = []
    while not stack.is_empty():
        reversed.append(stack.pop())
    return ''.join(reversed)


class Stack():
    def __init__(self):
        self.top = -1
        self.array = []

    def push(self, x):
        self.array.append(x)

    def pop(self):
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("geekforgeeks"))