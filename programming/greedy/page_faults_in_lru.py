"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
from collections import deque
def main(pages, c):
    pq = deque()
    faults = c
    i, k = 0, 0
    while k < c:
        if pages[i] not in list(pq):
            pq.append(pages[i])
            k += 1
        i += 1
    for j in range(c, len(pages)):
        page_exists = False
        for qitem in list(pq):
            if qitem == pages[j]:
                page_exists = True
                pq.append(pq.popleft())
        if not page_exists:
            pq.popleft()
            pq.append(pages[j])
            faults += 1
    return faults



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 2, 1, 4, 2, 3, 5], 3)) # 8
print(main([5, 0, 1, 3, 2, 4, 1, 0, 5], 4)) # 8
print(main([2, 3, 1, 3, 1, 3, 1, 2], 3)) # 3