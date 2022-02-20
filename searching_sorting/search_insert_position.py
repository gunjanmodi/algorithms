from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    closest_index = 0
    difference = float("inf")
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            current_difference = abs(target - nums[mid])
            if current_difference < difference:
                closest_index = left
            left += 1
        elif nums[mid] > target:

            current_difference = abs(nums[mid] - target)
            if current_difference < difference:
                closest_index = right
            right -= 1
        else:
            return mid
    return closest_index