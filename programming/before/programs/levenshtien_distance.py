def levenshteinDistance(str1,str2):
    dp = []
    dp.append([y for y in range(len(str2) + 1)])
    for x in range(len(str1)):
        dp.append([0 for y in range(len(str2) + 1)])

    for t in range(len(str1)+1):
        dp[t][0] = t
    
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    return dp[len(str1)][len(str2)]
    
if __name__ == '__main__':
    levenshteinDistance("abd", "yabc")