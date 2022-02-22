"""
Given an array of integers, return array element of triplets
such that they add up to a specific target.
Example:
    Given nums = [12, 3, 1, 2, -6, 5, -8, 6], target = 0,
    return: [[-8, 2, 6], [-8, 3, 5],[-6, 1, 5]]
"""

from typing import List


# def three_number_sum(nums: List[int], target: int) -> List[List[int]]:
#     nums.sort()
#     result = []
#     for i in range(len(nums)-2):
#         left = i + 1
#         right = len(nums) - 1
#
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
#             if current_sum == target:
#                 result.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#             if current_sum > target:
#                 right -= 1
#             if current_sum < target:
#                 left += 1
#     return result



def three_number_sum_1(A, X):
    set_a = set(A)
    counter = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            reminder = abs(A[i] + A[j] - X)
            if reminder in set_a:
                counter += 1
    return 1 if counter > 0 else 0



# three_number_sum([12, 3, 1, 2, -6, 5, -8, 6])
print(three_number_sum_1([1, 4, 45, 6, 10, 8], 13))





















