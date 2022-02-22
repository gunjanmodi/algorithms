"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def four_sum(array, target):
    result = []
    pairs_dict = {}
    for i in range(1, len(array)):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            difference = target - current_sum
            if difference in pairs_dict:
                for pair in pairs_dict[difference]:
                    quadruple = pair+[array[i], array[j]]
                    quadruple.sort()
                    result.append(quadruple)

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pairs_dict:
                pairs_dict[current_sum] = [[array[i], array[k]]]
            else:
                pairs_dict[current_sum].append([array[i], array[k]])
    result.sort()
    return result


def fourSum(nums, target):
    nums.sort()
    sum_reference = {}
    result = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            left, right = j + 1, len(nums) - 1
            reminder = target - nums[i] - nums[j]
            while left < right:
                if nums[left] + nums[right] == reminder:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > reminder:
                    right -= 1
                else:
                    left += 1
    return result





# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main([88, 84, 3, 51, 54, 99, 32, 60, 76, 68, 39, 12, 26, 86, 94, 39, 95, 70, 34, 78, 67, 1, 97, 2, 17, 92, 52], 179))
# print(main([7, 6, 4, -1, 1, 2], 16))