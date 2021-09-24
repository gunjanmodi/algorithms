def shortest_common_super_sequence(x, y):
    m = len(x)
    n = len(y)

    # dp[i][j] contains length of shortest
    # supersequence for X[0..i-1] and Y[0..j-1]
    dp = [[0 for i in range(n + 1)]
          for j in range(n + 1)]

    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # Below steps follow recurrence relation
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1])

    # Following code is used to print
    # shortest supersequence

    # dp[m][n] stores the length of the
    # shortest supersequence of X and Y
    for i in dp:
        print(i)
    # string to store the shortest supersequence
    string = ""

    # Start from the bottom right corner and
    # one by one push characters in output string
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X and Y are same,
        # then current character is part of
        # shortest supersequence
        if x[i - 1] == y[j - 1]:

            # Put current character in result
            string += x[i - 1]

            # reduce values of i, j and index
            i -= 1
            j -= 1

        # If current character in X and Y are different
        elif dp[i - 1][j] > dp[i][j - 1]:

            # Put current character of Y in result
            string += y[j - 1]

            # reduce values of j and index
            j -= 1
        else:

            # Put current character of X in result
            string += x[i - 1]

            # reduce values of i and index
            i -= 1

    # If Y reaches its end, put remaining characters
    # of X in the result string
    while i > 0:
        string += x[i - 1]
        i -= 1

    # If X reaches its end, put remaining characters
    # of Y in the result string
    while j > 0:
        string += y[j - 1]
        j -= 1

    string = list(string)

    # reverse the string and return it
    string.reverse()
    return ''.join(string)


def shortest_common_super_sequence2(string1, string2):
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

    print("------------------- ")
    for i in t:
        print(i)
    # print("SCS Length ", m + n - t[-1][-1])
    return build_sequence(string1, string2, m, n, t)


def build_sequence(string1, string2, i, j, t):
    result = []
    while i > 0 and j > 0:
        if string1[i - 1] == string2[j - 1]:
            result.append(string1[i - 1])
            i -= 1
            j -= 1

        elif t[i][j - 1] > t[i - 1][j]:
            result.append(string1[i - 1])
            i -= 1
        else:
            result.append(string2[j - 1])
            j -= 1

    while i > 0:
        result.append(string2[i - 1])
        i -= 1

    while j > 0:
        result.append(string2[j - 1])
        j -= 1

    result.reverse()
    return ''.join(result)


if __name__ == '__main__':
    print(shortest_common_super_sequence("AGGTAB", "GXTXAYB"))
    print(shortest_common_super_sequence2("AGGTAB", "GXTXAYB"))

    # print(shortest_common_super_sequence("acbcf", "abcdaf"))
    # print(shortest_common_super_sequence("HELLO", "GEEK"))

    # print(shortest_common_super_sequence("efgh", "jghi"))