from calendar import c
from platform import architecture
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            count += 1
        return count

        
if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([1,2], 3)) # 1
    print(s.numRescueBoats([3,2,2,1], 3)) # 3
    print(s.numRescueBoats([3,5,3,4], 5)) # 4 
    print(s.numRescueBoats([5,1,4,2], 6)) # 2
    print(s.numRescueBoats([5,1,7,4,2,4], 7)) # 4
    print(s.numRescueBoats([7, 3, 2], 8)) # 4