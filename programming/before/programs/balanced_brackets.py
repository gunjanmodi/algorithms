import unittest

def balanced_brackets(string):
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_pair = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            if matching_pair[char] == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balanced_brackets("([])(){}(())()()"), True)

if __name__ == '__main__':
    unittest.main()