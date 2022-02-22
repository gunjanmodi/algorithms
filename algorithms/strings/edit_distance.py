def levenshtein_distance(string1, string2):
    dp = []
    for i in range(len(string1)+1):
        dp.append([0]*(len(string2)+1))
    for i in range(len(string2)+1):
        dp[0][i] = i
    for i in range(len(dp)):
        dp[i][0] = i


    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

    return dp[-1][-1]


levenshtein_distance("abc", "yabd")
