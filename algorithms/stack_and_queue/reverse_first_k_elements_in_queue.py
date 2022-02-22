"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

from queue import Queue
# Time: O(n) | Space: O(n)
def main(queue, k):
    stack = []
    temp_queue = Queue()
    for i in range(k):
        stack.append(queue.get())
    while not queue.empty():
        temp_queue.put(queue.get())
    while len(stack) > 0:
        queue.put(stack.pop())
    while not temp_queue.empty():
        queue.put(temp_queue.get())
    return queue



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print(main(q, 3))