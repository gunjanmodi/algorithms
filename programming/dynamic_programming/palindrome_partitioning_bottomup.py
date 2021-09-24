"""
Format to solve:
Pattern: MCM
1. Find i/j
2. BC
3. k loop figure out
4. set minimum answer
"""


def palindrome_partitioning(string):
    t = []
    for _ in range(len(string)):
        t.append([-1 for __ in range(len(string))])
    return palindrome_partitioning_helper(string, 0, len(string) - 1, t)


def palindrome_partitioning_helper(string, i, j, t):
    if i >= j or is_palindrome(string[i: j + 1]):
        return 0
    if t[i][j] != -1:
        return t[i][j]
    min_answer = float('inf')
    for k in range(i, j):
        # temp_answer = 1 +\
        #               palindrome_partitioning_helper(string, i, k, t) +\
        #               palindrome_partitioning_helper(string, k + 1, j, t)
        if t[i][k] != -1:
            left = t[i][k]
        else:
            left = palindrome_partitioning_helper(string, i, k, t)
            t[i][k] = left

        if t[k + 1][j] != -1:
            right = t[k + 1][j]
        else:
            right = palindrome_partitioning_helper(string, k + 1, j, t)

        temp_answer = 1 + left + right
        min_answer = min(min_answer, temp_answer)
        t[i][j] = min_answer
    return min_answer

def is_palindrome(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(palindrome_partitioning("nitin"))
    print(palindrome_partitioning("nitik"))
    print(palindrome_partitioning("noonabbad"))