import unittest

def knuth_morris_pratt_algorithm(string, substring):
    pattern = build_pattern(substring)
    return does_match(string, substring, pattern)

def build_pattern(substring):
	pattern = [-1 for i in substring]
	i = 1
	j = 0
	while i < len(substring):
		if substring[i] == substring[j]:
			pattern[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return pattern

def does_match(string, substring, pattern):
	i = 0
	j = 0
	while i + len(substring) - j <= len(string):
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return False


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knuth_morris_pratt_algorithm("aefaefaefaedaefaedaefaefa", "aefaedaefaefa"), True)

if __name__ == '__main__':
    unittest.main()