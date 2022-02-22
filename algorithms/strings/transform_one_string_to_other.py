"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(string1, string2):
    if len(string1) != len(string2):
        return -1
    string1 = list(string1)
    string2 = list(string2)
    count = 0
    i = len(string1) - 1
    while i >= 0:
        if string1[i] == string2[i]:
            i -= 1
        else:
            j, k = i, i - 1
            while k >= 0:
                string1[j], string1[k] = string1[k], string1[j]
                j -= 1
                k -= 1
            count += 1
    return count


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("ABD", "BAD"))
print(main("EACBD", "EABCD"))
