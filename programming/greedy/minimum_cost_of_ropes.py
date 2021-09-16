"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
from heapq import heapify, heappush, heappop
def main(ropes):
    heapify(ropes)
    total_cost = 0
    while len(ropes) > 1:
        first = heappop(ropes)
        second = heappop(ropes)
        current_total = first + second
        total_cost += current_total
        heappush(ropes, current_total)
    # if ropes:
    #     total_cost += sum(ropes)
    return total_cost


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([4, 3, 2, 6]))
print(main([4, 2, 7, 6, 9]))