class Stack:
    def __init__(self):
        self.array = []

    def get_middle_index(self):
        return self.length() // 2 + 1


    def push(self, element):
        self.array.append(element)

    def pop(self):
        if self.length() > 0:
            return self.array.pop()
        return -1

    def length(self):
        return len(self.array)

    def top(self):
        if self.length() > 0:
            return self.array[-1]
        return -1