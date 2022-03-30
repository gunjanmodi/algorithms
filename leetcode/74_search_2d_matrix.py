from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 1:
            i = -1
        else:
            i = 0
            j = m - 1
            k = n - 1
            while i <= j:
                mid = (i + j ) // 2
                if target <= matrix[mid][k]:
                    j = mid - 1
                else:
                    i = mid + 1
        
        if i >= m:
            return False
        row = matrix[i]
        i = 0
        j = len(row) - 1
        while i <= j:
            mid = (i + j) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
                
        return False
        

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
    print(s.searchMatrix([[1,3]],3))
    print(s.searchMatrix([[1],[3],[5]],3))
    print(s.searchMatrix([[1]],3))
    print(s.searchMatrix([[1], [3]], 4))