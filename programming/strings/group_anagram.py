"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(words):
    reference = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in reference:
            reference[key].append(word)
        else:
            reference[key] = [word]
    return list(reference.values())


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(['act', 'god', 'cat', 'dog', 'tac']))
