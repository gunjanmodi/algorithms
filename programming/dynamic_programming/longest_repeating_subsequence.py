def longest_repeating_subsequence(string):
    string1 = string
    string2 = string
    t = []
    m = len(string1)
    n = len(string2)

    for i in range(m + 1):
        t.append([0 for _ in range(n + 1)])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1] and i != j:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[-1][-1]


if __name__ == '__main__':
    print(longest_repeating_subsequence("AABEBCDD"))
    print(longest_repeating_subsequence("axxxy"))