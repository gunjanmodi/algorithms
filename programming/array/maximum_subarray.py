from typing import List

def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return sum(nums)
    p1, p2 = 0, 1
    max_sum = float("-inf")
    i = 0
    while i < len(nums) - 2:
        current_sum = nums[p1] + nums[p2]
        if current_sum > max_sum:
            max_sum = current_sum
            p2 += 1
        else:
            i = p2 + 1
            p1 = i
            p2 = i + 1
    return max_sum


maxSubArray([5,4,-1,7,8])
