"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O() | Space: O()
from queue import Queue
def main(queue):
    stack = []
    half_size = queue.qsize() // 2
    for i in range(half_size):
        stack.append(queue.get())
    while len(stack) > 0:
        queue.put(stack.pop())
    for i in range(half_size):
        queue.put(queue.get())
    for i in range(half_size):
        stack.append(queue.get())
    while len(stack) > 0:
        queue.put(stack.pop())
        queue.put(queue.get())
    print(queue)



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
q = Queue()
q.put(11)
q.put(12)
q.put(13)
q.put(14)
q.put(15)
q.put(16)
q.put(17)
q.put(18)
q.put(19)
q.put(20)

print(main(q))