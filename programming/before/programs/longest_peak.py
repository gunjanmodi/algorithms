import unittest

def longest_peak(array):
    longest_peak_length = 0
    i = 1
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i + 1] < array[i]
        if not is_peak:
            i += 1
            continue
        
        left_idx = i - 2
        while left_idx >=0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1
            
        current_peak_length = right_idx - left_idx - 1
        longest_peak_length = max(current_peak_length, longest_peak_length)
        i = right_idx
    return longest_peak_length
        


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longest_peak(array), expected)


if __name__ == '__main__':
    unittest.main()