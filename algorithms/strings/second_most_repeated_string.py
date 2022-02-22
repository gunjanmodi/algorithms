"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O()
# Space: O()
def main(array):
    reference = {}
    ranking = [[float('-inf'), ""], [float('-inf'), ""]]
    first, second = 0, 1
    for string in array:
        reference[string] = reference.get(string, 0) + 1
        if reference[string] > ranking[first][0]:
            ranking[second][0] = ranking[first][0]
            ranking[second][1] = ranking[first][1]
            ranking[first][0] = reference[string]
            ranking[first][1] = string
        elif reference[string] > ranking[second][0] and reference[string] < ranking[first][0] and ranking[first][1] != ranking[second][1]:
            ranking[second][0] = reference[string]
            ranking[second][1] = string
    return ranking[-1][-1]


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print(main(['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']))
print(main(['geek', 'for', 'geek', 'for', 'geek', 'aaa']))
