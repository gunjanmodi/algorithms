def min_operations(s1, s2):
    m = len(s1)
    n = len(s2)
    lcs = longest_common_subsequence(s1, s2, m, n)
    return m - lcs + n - lcs
    
def longest_common_subsequence(self, s1, s2, m, n):
    t = []
    for i in range(m + 1):
        t.append([0 for _ in range(n + 1)])
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
            
    return t[-1][-1]