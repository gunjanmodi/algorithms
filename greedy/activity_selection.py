"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O(nlogn) | Space: O(n)
def main(start, end):
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])
    count = 1
    start, end = 0, 1
    previous = meetings[0]
    for i in range(1, len(meetings)):
        current = meetings[i]
        if current[start] > previous[end]:
            count += 1
            previous = current
    return count


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1,3,0,5,8,5], [2,4,6,7,9,9]))
print(main([10, 12, 20], [20, 25, 30]))
print(main([3, 2, 1, 10], [8, 4, 3, 11]))