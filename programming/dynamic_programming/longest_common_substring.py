def longest_common_substring(string1, string2):
    m = len(string1)
    n = len(string2)
    max_so_far = 0
    t = []
    for i in range(m + 1):
        t.append([0 for _ in range(n + 1)])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = 0
            max_so_far = max(max_so_far, t[i][j])

    return max_so_far


if __name__ == '__main__':
    print(longest_common_substring("abcde", "abfce"))