"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
class TwoStacks():
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = x
        else:
            print('Stack Overflow')

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = x
        else:
            print('Stack Overflow')


    def pop1(self):
        if self.top1 >= 0:
            element = self.array[self.top1]
            self.top1 -= 1
            return element
        else:
            print('Stack Overflow')

    def pop2(self):
        if self.top2 < self.size:
            element = self.array[self.top2]
            self.top2 += 1
            return element
        else:
            print('Stack Overflow')



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
stack = TwoStacks(5)
stack.push1(2)
stack.push1(3)
stack.push2(4)
stack.pop2()
stack.pop2()