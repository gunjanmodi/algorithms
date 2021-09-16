
"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O(n)
# Space: O(n)


def main(string):
    pattern = [-1 for _ in string]
    i, j = 1, 0
    while i < len(string):
        if string[i] == string[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return string[0:pattern[-1] + 1]

print(main("leetcode")) # ""
print(main("babbb"))  # b
# Test case 1: Normal or Given input
print(main("leetcodeleet")) # "leet"
# Test case 2: Normal or Given input
print(main("ababab")) # "abab"
# Test case 3: Normal or Given input
print(main("level")) # "l"
# Test case 4: Negative
print(main("u")) # ""
# Test case 5: Empty
print(main("ab"))
# Test case 6: Too long
# print(main())
# Test case 7
# Test case 8
# Test case 9