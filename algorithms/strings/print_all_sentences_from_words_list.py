"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(words_list):
    result = []
    print_sentence_helper(words_list, result, [], 0)
    return result


def print_sentence_helper(words_list, result, current, c):
    if len(current) == len(words_list):
        result.append(' '.join(current))
        if len(current) > 0:
            current.pop()
            return
    words = words_list[c]
    for word in words:
        current.append(word)
        print_sentence_helper(words_list, result, current, c+1)
    if len(current) > 0:
        current.pop()


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([["you", "we"], ["have", "are"], ["sleep", "eat", "drink"]]))
print(main([["you", "we"], ["have", "are"], ["sleep", "eat", "drink"], ["peacefully", "too much"], ["John", "Jani", "Janardan"]]))
