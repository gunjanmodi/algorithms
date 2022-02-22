def longest_palindrome(string):
    longest = [0, 1]
    for i in range(1, len(string)): # O(n), O(1)
        current = get_longest_palindrome(string, i, i)
        longest = max(longest, current, key=lambda x:x[1]-x[0])
        current = get_longest_palindrome(string, i, i + 1)
        longest = max(longest, current, key=lambda x:x[1]-x[0])
    return string[longest[0]:longest[1]] # O(n), O(n)


def get_longest_palindrome(string, left, right): # O(n), O(1)
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return [left+1, right]





print(longest_palindrome("aaaabbaa"))
print(longest_palindrome("abc"))
print(longest_palindrome("abaxyzzyxf"))  # xyzzyx
