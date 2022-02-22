import unittest


def top_two(nums):
    # first, second = float('-inf'), float('-inf')
    bounds = [-1, -1]
    for num in nums:
        update_nums(num, bounds)
    return bounds

def update_nums(num, bounds):
    if num > bounds[0]:
        bounds[1] = bounds[0]
        bounds[0] = num
    elif num > bounds[1] and bounds[0] != num:
        bounds[1] = num

    if bounds[1] == bounds[0]:
        bounds[1] = -1


class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     output = top_two([1,4,45,6,10,8])
    #     self.assertEqual(output, [45,10])
    #
    # def test_case_2(self):
    #     output = top_two([1000, 1000, 1000, 1000, 1000, 100])
    #     self.assertEqual(output, [1000, 100])

    # def test_case_3(self):
    #     output = top_two([2, 1, 2])
    #     self.assertEqual(output, [2, 1])

    def test_case_4(self):
        output = top_two([10, 10, 10, 10, 10, 10])
        self.assertEqual(output, [10, -1])



if __name__ == '__main__':
    unittest.main()


