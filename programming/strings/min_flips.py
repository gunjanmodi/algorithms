"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""

# Time: O()
# Space: O()
def main(string):
    count0, count1 = 0, 0
    toggle0, toggle1 = '0', '1'
    for i in range(len(string)):
        if string[i] != toggle0:
            count0 += 1
        if string[i] != toggle1:
            count1 += 1
        toggle0 = '1' if toggle0 == '0' else '0'
        toggle1 = '1' if toggle0 == '0' else '0'
    return min(count0, count1)


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("01001001101"))
print(main("1111110000000000000"))
print(main("0001010111"))
print(main("001"))
