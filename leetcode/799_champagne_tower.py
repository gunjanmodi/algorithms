from tempfile import tempdir


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        matrix = [[0 for _ in range(i)] for i in range(1, query_row+2)]
        matrix[0][0] = poured
        for i in range(query_row):
            for j in range(len(matrix[i])):
                percent = (matrix[i][j] - 1) / 2.0 
                if percent > 0:
                    matrix[i+1][j] += percent 
                    matrix[i+1][j+1] += percent
        return matrix[query_row][query_glass] if matrix[query_row][query_glass] <= 1 else 1




if __name__ == '__main__':
    s = Solution()
    print(s.champagneTower(100000009, 33, 17))