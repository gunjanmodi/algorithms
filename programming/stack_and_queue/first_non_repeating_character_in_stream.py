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
def main(string):
    dq = deque()
    ref = {}
    repeated_chars = set()
    result = []
    for i, char in enumerate(string):
        dq.append(char)
        outcome = '#'
        if char not in ref:
            ref[char] = 1
        else:
            ref[char] += 1
            repeated_chars.add(char)

        while dq and dq[0] in repeated_chars:
            dq.popleft()
        if dq:
            outcome = dq[0]
        result.append(outcome)
    return ''.join(result)
# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("ftvbwnimpvvbfvtot")) # ffffffffffffttwww
# print(main("aabc")) # a#b#ccdd
# print(main("zz")) # a#b#ccdd
# print(main("aabbcdcz")) # a#b#ccdd