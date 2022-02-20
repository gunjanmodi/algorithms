"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(wild, pattern):
    wild = list(wild)
    pattern = list(pattern)
    if not len(wild) or not len(pattern):
        return False
    i = 0
    while i < len(wild) and i < len(pattern):
        if wild[i] == pattern[i]:
            i += 1
        elif wild[i] == '?':
            wild[i] = pattern[i]
            i += 1
        else:
            i += 1

    return wild == pattern


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main('a', 'aa'))
print(main('?a', 'cb'))
# print(main('ge*ks', 'geeks'))
# print(main('ge?ks*', 'geeksforgeeks'))
# print(main('geeks', 'geeksforgeeks'))
# print(main('ge?ks*', ''))
# print(main('', 'geeksforgeeks'))
# print(main('gee??for*', 'geeksforgeeks'))
# print(main('geek*s?', 'geekforgeek'))

