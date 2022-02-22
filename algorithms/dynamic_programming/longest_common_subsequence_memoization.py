def lcs(string1, string2):
    m = len(string1)
    n = len(string2)
    t = []

    t = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    return lcs_helper(string1, string2, m, n, t)

def lcs_helper(string1, string2, m, n, t):
    if m == 0 or n == 0:
        return 0

    if t[m - 1][n - 1] < 0:
        if string1[m - 1] == string2[n - 1]:
            t[m - 1][n - 1] = 1 + lcs_helper(string1, string2, m - 1, n - 1, t)
        else:
            t[m - 1][n - 1] = max(
                lcs_helper(string1, string2, m - 1, n, t),
                lcs_helper(string1, string2, m, n - 1, t)
            )
    return t[m - 1][n - 1]



def lcs(s1, s2, p1, p2, t):
    key = (p1 - 1, p2 - 1)
    if key in t:
        return t[key]
    if p1 == 0 or p2 == 0:
        return 0
    if s1[p1 - 1] == s2[p2 - 1]:
        t[key] = 1 + lcs(s1, s2, p1 - 1, p2 - 1, t)
    else:
        t[key] = max(lcs(s1, s2, p1 - 1, p2, t), lcs(s1, s2, p1, p2 - 1, t))
    return t[key]


def longestCommonSubsequence(str1, str2):
    t = {}
    p1 = len(str1)
    p2 = len(str2)
    return lcs(str1, str2, p1, p2, t)



if __name__ == '__main__':
    print(longestCommonSubsequence("ABCDGH", "AEDFHR"))
    print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))
