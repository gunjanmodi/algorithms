from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search([-1,0,3,5,9,12], 2))