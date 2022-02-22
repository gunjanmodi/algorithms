def palindrome_partition(s):
    result = []
    backtack(result, [], s, 0)
    return result

def backtack(result, temp_list, s, start):
    if start == len(s):
        result.append(temp_list[:])
    else:
        for i in range(start, len(s)):
            if is_palindrome(s, start, i):
                temp_list.append(s[start:i + 1])
                backtack(result, temp_list, s, i + 1)
                temp_list.pop(-1)

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    
print(palindrome_partition("aab"))