import unittest

def same_bsts(array_one, array_two):
    if len(array_one) != len(array_two):
        return False
    
    if len(array_one) == 0 and len(array_two) == 0:
        return True

    if array_one[0] != array_two[0]:
        return False

    left_one = get_smaller(array_one)
    left_two = get_smaller(array_two)
    right_one = get_bigger_or_equal(array_one)
    right_two = get_bigger_or_equal(array_two)

    return same_bsts(left_one, left_two) and same_bsts(right_one, right_two)

def get_smaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def get_bigger_or_equal(array):
    bigger_or_equal = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger_or_equal.append(array[i])
    return bigger_or_equal

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        self.assertEqual(same_bsts(array_one, array_two), True)

if __name__ == '__main__':
    unittest.main()