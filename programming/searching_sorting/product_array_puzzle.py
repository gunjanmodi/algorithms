"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(nums):
    prod = 1
    flag = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            flag += 1
        else:
            prod *= nums[i]
    array = [0 for _ in nums]
    for i in range(len(nums)):
        if flag > 1:
            array[i] = 0
        elif flag == 0:
            array[i] = prod // nums[i]
        elif flag == 1 and nums[i] != 0:
            array[i] = 0
        else:
            array[i] = prod

    return array


# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([1, 0]))