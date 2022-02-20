"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# I/P - O/P Method of Recursion

# Time: O() | Space: O()
def subset(string):
    result = []
    result = subset_helper(string, "", result)
    return result


def subset_helper(string, new_string, result):
    if len(string) == 0:
        result.append(new_string)
        return result
    top = string[0]
    string = string[1:]
    result = subset_helper(string, new_string, result)
    new_string += top
    result = subset_helper(string, new_string, result)
    return result


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(subset("abc"))
# print(subset("abcd"))
# print(subset(""))
# print(subset("abcdefghijk"))
# print(subset("aab"))