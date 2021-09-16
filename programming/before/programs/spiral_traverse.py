import unittest

def spiral_traverse(mattrix):
    start_row, end_row = 0, len(mattrix) - 1
    start_col, end_col = 0, len(mattrix[0]) - 1
    result = []

    while start_row <= end_row and start_col <= end_col:
        for i in range(start_col, end_col + 1):
            result.append(mattrix[start_row][i])
        for j in range(start_row + 1, end_row + 1):
            result.append(mattrix[j][end_col])
        for k in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(mattrix[end_row][k])
        for l in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(mattrix[l][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    print(result)
    
    return result

        




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        matrix = [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]
        # expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        self.assertEqual(spiral_traverse(matrix), expected)

if __name__ == '__main__':
    unittest.main()