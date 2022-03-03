from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        answer = 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                memo[i] = memo[i-1] + 1
            answer += memo[i]
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1,2,3,8,9,10]))
    print(s.numberOfArithmeticSlices([1]))
    print(s.numberOfArithmeticSlices([1, -10]))
    print(s.numberOfArithmeticSlices([1,3,5,7,9]))
    print(s.numberOfArithmeticSlices([3,-1,-5,-9]))
    print(s.numberOfArithmeticSlices([1,2,3,8,9,10]))
                    
        