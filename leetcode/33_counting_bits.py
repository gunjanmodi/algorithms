"""
Given an integer n, return an array ans of length n + 1,
such that for each i (0 <= i <= n), ans[i] is the number
of 1's in the binary representation of i.
n = 2, [0,1,1]
n = 5, [0,1,1,2,1,2]
"""


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        cache = {0:0, 1:1}
        result = [None for _ in range(n+1)]
        
        def solve(n):
            answer = None
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
                
            if n % 2 == 0:
                cache[n] = solve(n//2)
            else:
                cache[n] = 1+ solve(n // 2)
            return cache[n]
            
        for i in range(n+1):
            result[i] = solve(i)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))
                
            

        