def lcs_recursive(s1, s2, m, n):
    sub_sequences = []
    
    if m == 0 or n == 0:
        return sub_sequences
    if s1[m-1] == s2[n-1]:
        sub_sequences.append(s1[m-1])
        return 1 + lcs(s1, s2, m-1, m-2)
    else:
        return max(
            lcs(s1, s2, m-1,n),
            lcs(s1, s2, m,n-1)
        )


def build_sequences(dp, str1):
    sequence = []
    i = len(dp) - 1
    j = len(dp[0]) - 1

    while i != 0 and j != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            sequence.append(str1[j-1])
            i -= 1
            j -= 1
    return list(reversed(sequence))

def lcs(str1, str2):
    dp = []
    for x in range(len(str2)+1):
        dp.append([0 for y in range(len(str1)+1)])

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return build_sequences(dp, str1)


if __name__ == '__main__':
    s1 = "AXYZ"
    s2 = "BAZ"
    print(lcs(s1, s2))