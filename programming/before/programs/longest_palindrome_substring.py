def longestPalindromicSubstring1(string):
    longest = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            current = string[i:j+1]
            if len(current) > len(longest) and is_palindrome(current):
                longest = current
    return longest

def is_palindrome(string):
	left = 0
	right = len(string) - 1
	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True


def longestPalindromicSubstring(string):
    current_longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome(string, i - 1, i + 1)
        even = get_longest_palindrome(string, i - 1, i)
        longest = max(odd, even, key=lambda  x: x[1]-x[0])
        current_longest = max(longest, current_longest, key=lambda x: x[1]-x[0])
    return string[current_longest[0] : current_longest[1]]

def get_longest_palindrome(string, left, right):
    while len(left) >= 0 and len(right) < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left - 1, right]



if __name__ == '__main__':
    longestPalindromicSubstring("abcba")


	
