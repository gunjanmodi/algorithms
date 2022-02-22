"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O(n) | Space: O(1)
def main(words):
    i = 0
    smallest_word = min(words, key=len)
    if not smallest_word:
        return ''
    for i in range(len(smallest_word)):
        for w in range(1, len(words)):
            prev_word = words[w-1]
            current_word = words[w]
            if prev_word[i] != current_word[i]:
                return current_word[:i]
    return smallest_word


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print("->", main(["cir", "car"]))
# print("->", main(["reflower","flow","flight"]))
print("->", main(["flower","flow","flight"]))
print("->", main([["dog","racecar","car"]]))
print("->", main([["a"]]))
print("->", main([[""]]))
