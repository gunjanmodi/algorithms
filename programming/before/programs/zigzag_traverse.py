import unittest

def zigzag_traverse(array):
    row, col = 0, 0
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    going_down = True
    while not is_out_of_bounds(row, col, height, width):
        result.append(array[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def is_out_of_bounds(row, col, height, width):
    return row < 0 or col > width or row > height or col < 0


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(zigzag_traverse(matrix), output)

if __name__ == '__main__':
    unittest.main()