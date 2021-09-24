def lcs(string1, string2):
    m = len(string1)
    n = len(string2)
    return lcs_helper(string1, string2, m, n)


def lcs_helper(string1, string2, m, n):
    if m == 0 or n == 0:
        return 0
    if string1[m - 1] == string2[n - 1]:
        return 1 + lcs_helper(string1, string2, m - 1, n - 1)
    else:
        return max(lcs_helper(string1, string2, m, n - 1), lcs_helper(string1, string2, m - 1, n))


if __name__ == '__main__':
    print(lcs("ZXVVYZW", "XKYKZPW"))
