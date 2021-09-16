"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(n):
    result = []
    recursive_helper(n, n, [], result)

    result2 = []
    recursive_helper2(n, n, [], result2)
    print(result)
    print(result2)
    return ''


def recursive_helper(o, c, output_string, result):
    if o == 0 and c == 0:
        result.append(''.join(output_string))
        return
    elif o == c:
        opening_handler(o, c, output_string, result)
    elif o == 0 and c > 0:
        closing_handler(o, c, output_string, result)
    else:
        output_string_copy = output_string[:]
        opening_handler(o, c, output_string, result)
        closing_handler(o, c, output_string_copy, result)

def recursive_helper2(o, c, output_string, result):
    if o == 0 and c == 0:
        result.append(''.join(output_string))
        return
    if o != 0:
        output_string_copy = output_string[:]
        opening_handler(o, c, output_string_copy, result)
    if c > o:
        output_string_copy = output_string[:]
        closing_handler(o, c, output_string_copy, result)


def opening_handler(o, c, output_string, result):
    output_string.append('(')
    recursive_helper(o - 1, c, output_string, result)


def closing_handler(o, c, output_string, result):
    output_string.append(')')
    recursive_helper(o, c - 1, output_string, result)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main(3))
