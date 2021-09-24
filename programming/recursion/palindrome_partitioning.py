"""
Format to solve:
Pattern: MCM
1. Find i/j
2. BC
3. k loop figure out
4. set minimum answer
"""


def palindrome_partitioning(string):
    return palindrome_partitioning_helper(string, 0, len(string) - 1)


def palindrome_partitioning_helper(string, i, j):
    if i >= j or is_palindrome(string[i: j + 1]):
        return 0
    min_answer = float('inf')
    for k in range(i, j):
        temp_answer = 1 +\
                      palindrome_partitioning_helper(string, i, k) +\
                      palindrome_partitioning_helper(string, k + 1, j)
        min_answer = min(min_answer, temp_answer)
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