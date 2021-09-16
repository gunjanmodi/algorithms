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
    recursive_helper("", string, result)
    return result


def recursive_helper(output_string, input_string, result):
    while input_string and input_string[0].isdigit():
        input_string = input_string[1:]

    if len(input_string) == 0:
        result.append(output_string)
        return

    output1 = f"{output_string}{input_string[0]}"
    if 65 <= ord(input_string[0]) < 97:  # capital
        output2 = f"{output_string}{input_string[0].lower()}"
    else:
        output2 = f"{output_string}{input_string[0].upper()}"

    input_string = input_string[1:]
    recursive_helper(output1, input_string, result)
    recursive_helper(output2, input_string, result)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("aB"))
print(main("a1B2c3"))
print(main("a111111111B2"))
print(main("11111a111B2"))
print(main("a111B2"))
