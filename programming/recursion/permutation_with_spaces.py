"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


"""
MAKE RECURSION TREE TO SOLVE THIS PROBLEM
"""


# Time: O() | Space: O()
def main(string):
    result = []
    if not len(string):
        return result
    recursive_helper(string[0], string[1:], result)
    return result


def recursive_helper(inp, string, result):
    if len(string) == 0:
        result.append(inp)
        return
    with_space_inp = f"{inp}_{string[0]}"
    without_space_inp = f"{inp}{string[0]}"
    string = string[1:]
    recursive_helper(with_space_inp, string, result)
    recursive_helper(without_space_inp, string, result)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("abc"))
print(main("abcd"))
print(main(""))
print(main("abcdefghijk"))