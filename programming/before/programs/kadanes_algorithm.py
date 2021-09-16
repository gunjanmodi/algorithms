import unittest

def kadanes_algorithm(array):
    max_ending_here = array[0]
    max_so_far = array[0]
    for num in array[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)

if __name__ == '__main__':
    unittest.main()