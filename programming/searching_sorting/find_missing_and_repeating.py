"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


from collections import Counter
# Time: O() | Space: O()
def main(array):
    counter = Counter(array)
    missing_num = -1
    repeating_num = -1
    num = 0
    while True:
        num += 1
        if missing_num == -1 and num not in counter:
            missing_num = num
        if counter.get(num, 0) >= 2:
            repeating_num = num
        if missing_num != -1 and repeating_num != -1:
            break
    return [repeating_num, missing_num]




# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 4, 5, 3, 3]))