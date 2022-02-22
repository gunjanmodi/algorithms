def shortest_common_super_sequence(string1, string2):
    m = len(string1)
    n = len(string2)
    t = []
    for i in range(m + 1):
        t.append([0 for _ in range(n + 1)])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])

    return m + n - t[-1][-1]


if __name__ == '__main__':
    print(shortest_common_super_sequence("acbcf", "abcdaf"))
    # print(shortest_common_super_sequence("abcd", "xycd"))
    # print(shortest_common_super_sequence("efgh", "jghi"))