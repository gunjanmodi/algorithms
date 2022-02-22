import unittest

def largest_range(array):
    nums = {}
    best_range = []
    largest_range_length = 0
    for num in array:
        nums[num] = False
    for num in array:
        if nums[num]:
            continue
        nums[num] = True
        left = num - 1
        current_length = 0
        while left in nums:
            nums[left] = True
            left -= 1
            current_length += 1
        right = num + 1
        while right in nums:
            nums[right] = True
            right += 1
            current_length += 1
        if current_length > largest_range_length:
            largest_range_length = current_length
            best_range = [left + 1, right - 1]
    return best_range

        

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
        self.assertEqual(largest_range(nums), [0, 7])


if __name__ == '__main__':
    unittest.main()