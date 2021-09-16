"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O() | Space: O()
def main(strings):
    if len(strings) == 1:
        return strings[-1][-1]
    min_string = min(strings, key=len)
    i = 0
    cp = ""
    # lcp = ""
    longest = ""
    while i < len(min_string):
        previous = strings[0]
        for s in range(1, len(strings)):
            current = strings[s]
            if current[i] == previous[i]:
                cp = current[i]
            else:
                longest = max(longest, cp, key=len)
                cp = ""
                # lcp = ""
                break
            previous = current
        # lcp += cp
        i += 1
    return longest


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print("->", main(["cir", "car"]))
# print("->", main(["reflower","flow","flight"]))
print("->", main(["flower","flow","flight"]))
print("->", main([["dog","racecar","car"]]))
print("->", main([["a"]]))
print("->", main([[""]]))
