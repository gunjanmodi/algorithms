import unittest

def water_area(heights):
    maxes = [0 for _ in heights]
    left_max = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = left_max
        left_max = max(height, left_max)
    
    right_max = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        min_height = min(maxes[i], right_max)
        if height < min_height:
            maxes[i] = min_height - height
        else:
            maxes[i] = 0
        right_max = max(right_max, height)
    return sum(maxes)    
        


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
        self.assertEqual(water_area(heights), 48)


if __name__ == '__main__':
    unittest.main()