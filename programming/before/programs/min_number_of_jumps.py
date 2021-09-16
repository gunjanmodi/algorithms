import unittest

# O(n^2) time | O(n) space
# def min_number_of_jumps(array):
#     jumps = [float('inf') for _ in array]
#     jumps[0] = 0
#     for i in range(len(array)):
#         for j in range(0, i):
#             if array[j] + j >= i:
#                 jumps[i] = min(jumps[i], jumps[j] + 1)
#     return jumps[-1]

# O(n) time | O(1) space
def min_number_of_jumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    max_reach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        current = array[i]
        max_reach = max(max_reach, current + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i
    return jumps + 1



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(min_number_of_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]), 4)

if __name__ == '__main__':
    unittest.main()