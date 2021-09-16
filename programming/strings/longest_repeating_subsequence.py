def longest_repeating_subsequence(string):
    n = len(string)
    dp = [[0 for k in range(n + 1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == string[j - 1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


print(longest_repeating_subsequence("axxxy"))
print(longest_repeating_subsequence("aab"))
print(longest_repeating_subsequence("jxyrnbvtfc"))
print(longest_repeating_subsequence("agcsorvauz"))