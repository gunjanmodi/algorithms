def lcs(string1, string2):
    m = len(string1)
    n = len(string2)
    t = []
    for i in range(m + 1):
        t.append([-1 for _ in range(n + 1)])

    return lcs_helper(string1, string2, m, n, t)
    # return t[-1][-1]


def lcs_helper(string1, string2, m, n, t):
    if m == 0 or n == 0:
        return 0

    if t[m - 1][n - 1] != -1:
        return t[m - 1][n - 1]

    if string1[m - 1] == string2[n - 1]:
        t[m - 1][n - 1] = 1 + lcs_helper(string1, string2, m - 1, n - 1, t)
        return t[m - 1][n - 1]
    else:
        t[m - 1][n - 1] = max(
            lcs_helper(string1, string2, m - 1, n, t),
            lcs_helper(string1, string2, m, n - 1, t)
        )
        return t[m - 1][n - 1]


if __name__ == '__main__':
    print(lcs("ABCDGH", "AEDFHR"))
    print(lcs("ZXVVYZW", "XKYKZPW"))
