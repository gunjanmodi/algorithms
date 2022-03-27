from heapq import heappop, heappush
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        num_of_soldiers = []
        heap = []
        for i in range(len(mat)):
            count_one = self.binary_search(mat[i])
            heappush(heap, (count_one, i))
            
        result = []
        while k:
            num, i = heappop(heap)
            result.append(i)
            k -= 1
        return result
    
    def binary_search(self, array):
        i = 0
        j = len(array) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if array[mid] == 1:
                i = mid + 1
            else:
                j = mid - 1
        return i
        
        
if __name__ == '__main__':
    s = Solution()
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]]
    k = 3
    print(s.kWeakestRows(mat, k))

    mat = [[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]]
    k = 2
    print(s.kWeakestRows(mat, k))
