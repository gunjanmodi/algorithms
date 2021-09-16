# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self._array = []
        self._top = -1
        self.max = None
        self.min = None

    def peek(self):
        # Write your code here.
        return self._array[self._top]

    def pop(self):
        # Write your code here.
        self._array.pop()

    def push(self, number):
        # Write your code here.
        self._array.append(number)
        if self.max is None:
            self.max = number
        else:
            self.max = max(self.max, number)
            
        if self.min is None:
            self.min = number
        else:
            self.min = min(self.min, number)

    def getMin(self):
        # Write your code here.
        return self.min

    def getMax(self):
        # Write your code here.
        return self.max


if __name__ == '__main__':
    stack = MinMaxStack()
    stack.push(5)
    print(stack.getMin())
    print(stack.getMax())
