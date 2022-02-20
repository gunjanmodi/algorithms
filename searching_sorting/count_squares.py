"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(a, b):
    count = 0
    for number in range(a, b + 1):
        j = 1
        while j <= number:
            if j * j == number:
                count += 1
            j += 1



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main())
