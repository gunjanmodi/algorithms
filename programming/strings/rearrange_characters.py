"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
import heapq
from collections import Counter


# def main(string):
#     res, c = [], Counter(string)
#     pq = [(-value, key) for key, value in c.items()]
#     heapq.heapify(pq)
#     p_a, p_b = 0, ''
#     while pq:
#         a, b = heapq.heappop(pq)
#         res += [b]
#         if p_a < 0:
#             heapq.heappush(pq, (p_a, p_b))
#         a += 1
#         p_a, p_b = a, b
#     res = ''.join(res)
#     if len(res) != len(string): return ""
#     return res

def main(string):
    result, counters = [], Counter(string)
    priority_queue = [(-value, key) for key, value in counters.items()]
    heapq.heapify(priority_queue)
    previous_value, previous_key = 0, ''
    while priority_queue:
        value, key = heapq.heappop(priority_queue)
        result.append(key)
        if previous_value < 0:
            heapq.heappush(priority_queue, (previous_value, previous_key))
        value += 1
        previous_value, previous_key = value, key
    result = ''.join(result)
    return result if len(result) == len(string) else ""


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long

print(main("bbbbb"))
print(main("vvvlo"))
print(main("aab"))
print(main("aaab"))
print(main("geekforgeeks"))
