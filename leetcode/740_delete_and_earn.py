from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cache = {}
        
        def solve(n):
            if n in cache:
                return cache[n]
            
            current = nums[n]
            if n == 0:
                return current * counter[current]
            
            previous = nums[n-1]
            if n == 1:
                if previous == current - 1:
                    return max(previous * counter[previous] , current * counter[current])
                else:
                    return previous * counter[previous] + current * counter[current]
                
            else:
                if previous == current - 1:
                    cache[n] = max(solve(n-1), solve(n-2) + current * counter[current])
                else:
                    cache[n] = solve(n-1) + current * counter[current]
                return cache[n]
        
        counter = Counter(nums)
        nums = sorted(counter.keys())
        return solve(len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn([3,4,2]))
    print(s.deleteAndEarn([2,2,3,3,3,4]))

