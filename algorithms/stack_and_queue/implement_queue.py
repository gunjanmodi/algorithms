"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            return item
        else:
            return "FULL"

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return -1

    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return -1

    def is_empty(self):
        return self.length() == 0

    def is_full(self):
        return self.length() >= self.max_size

    def length(self):
        return len(self.queue)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
queue = Queue(4)
print(queue.enqueue(10))
print(queue.enqueue(20))
print(queue.enqueue(30))
print(queue.enqueue(40))
print(queue.dequeue())
print(queue.enqueue(50))
print(queue.front())
print(queue.rear())