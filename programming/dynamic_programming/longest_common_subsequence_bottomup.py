def lcs(string1, string2):
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

    return build_sequence(t, string1, string2, m, n)


def build_sequence(t, string1, string2, i, j):
    result = []
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            result.append(string1[i - 1])
            i -= 1
            j -= 1
        else:
            if t[i][j - 1] > t[i - 1][j]:
                j -= 1
            else:
                i -= 1
    result.reverse()
    return "".join(result)
    # return t[-1][-1]


if __name__ == '__main__':
    print(lcs("abcd", "dcba"))
    print(lcs("axy", "adxcpy"))
    print(lcs("acbcf", "abcdaf"))
    print(lcs("ZXVVYZW", "XKYKZPW"))
    print(lcs("abcde", "abfce"))
    print(lcs("heap", "pea"))
