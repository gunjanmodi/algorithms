import unittest

def isMonotonic(array):
	if len(array) <= 2:
		return True
	
	direction = array[1] - array[0]
	for i in range(2, len(array)):
		if direction == 0:
			direction = array[i] - array[i - 1]
			continue
		if direction < 0 and array[i] > array[i - 1]:
			return False
		if direction > 0 and array[i] < array[i - 1]:
			return False
	return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        actual = isMonotonic(array)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()