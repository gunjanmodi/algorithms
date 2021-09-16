import unittest

def smallestSubstringContaining(bigString, smallString):
    target_char_counts = get_char_counts(smallString)
    substring_bounds = get_substring_bounds(bigString, target_char_counts)
    return get_string_from_bounds(bigString, substring_bounds)
    
    
def get_char_counts(string):
    char_counts = {}
    for char in string:
        increase_char_count(char, char_counts)
    return char_counts

def get_substring_bounds(string, target_char_counts):
    substring_bounds = [0, float("inf")]
    substring_char_counts = {}
    num_unique_chars = len(target_char_counts.keys())
    num_unique_chars_done = 0
    left_idx = 0
    right_idx = 0
    
    while right_idx < len(string):
        right_char = string[right_idx]
        if right_char not in target_char_counts:
            right_idx += 1
            continue
        increase_char_count(right_char, substring_char_counts)
        if substring_char_counts[right_char] == target_char_counts[right_char]:
            num_unique_chars_done += 1
            
        while num_unique_chars_done == num_unique_chars and left_idx <= right_idx:
            substring_bounds = get_closer_bounds(left_idx, right_idx, substring_bounds[0], substring_bounds[1])
            left_char = string[left_idx]
            if left_char not in target_char_counts:
                left_idx += 1
                continue
            decrease_char_count(left_char, substring_char_counts)
            left_idx += 1
        right_idx += 1
    return substring_bounds
        
def get_string_from_bounds(string, bounds):
    start, end = bounds
    if end == float("inf"):
        return ""
    return string[string : end + 1]
    
def get_closer_bounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]
    
def increase_char_count(char, char_counts):
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1
    
def decrease_char_count(char, char_counts):
    char_counts[char] -= 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        big_string = "abcd$ef$axb$c$"
        small_string = "$$abf"
        expected = "f$axb$"
        self.assertEqual(smallestSubstringContaining(big_string, small_string), expected)


if __name__ == '__main__':
    unittest.main()