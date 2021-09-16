"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
'''
def main(string):
    # string_array = list(string)
    # i = len(string_array) - 2
    # while i >= 0:
    #     if string_array[i] == string_array[i+1]:
    #         string_array[i] = None
    #         i -= 1
    #     i -= 1
    # string_array = [chr for chr in string_array if chr]
    # return ''.join(string_array)
    n = len(string)
    string = list(string)
    if (n < 2):
        return

        # j is used to store index is result
    # string (or index of current distinct
    # character)
    j = 0

    # Traversing string
    for i in range(n):

        # If current character S[i]
        # is different from S[j]
        if (string[j] != string[i]):
            j += 1
            string[j] = string[i]

    # Putting string termination
    # character.
    j += 1
    string = string[:j]
    return string
'''


def main(string):
    stack = []
    for i in range(len(string)):
        character = string[i]
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)
    return ''.join(stack)




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("abbaca"))
print(main("azxxzy"))
