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
    left, right = 0, 0
    swap, balance = 0, 0
    for character in string:
        if character == '[':
            left += 1
            if balance > 0:
                swap += 1
                balance -= 1
        elif character == ']':
            right += 1
            balance = right - left
    return swap

# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
# print(main("[]][]["))
# print(main("[[][]]"))
print(main("]["))
