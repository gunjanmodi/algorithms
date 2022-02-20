"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(string):
    string_list = list(string)
    string_list.reverse()
    new_part = []
    i, j = 0, len(string_list) - 1
    while i <= j:
        left = string_list[i]
        right = string_list[j]
        if left != right:
            new_part.append(string_list[i])
            i += 1
        else:
            i += 1
            j -=1
    return len(new_part)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("geeks"))
print(main("abcd"))
print(main("aa"))
