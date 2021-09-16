from palindrome_check import is_palindrome

def palindrome_partitioning_min_cuts(string):
    dp = []
    for i in range(len(string)):
        dp.append([True if i == x else False  for x in range(len(string))])

    for i in range(len(string)):
        for j in range(i, len(string)):
            dp[i][j] = is_palindrome(string[i:j+1])

    cuts = [float("inf") for i in string]
    
    for i in range(len(string)):
        if dp[0][i]:
            cuts[i] = 0
        else:
            cuts[i] = cuts[i-1] + 1
            for j in range(1, i):
                if dp[j][i] and cuts[j-1] + 1 < cuts[i]:
                    cuts[i] = cuts[j-1] + 1

    return cuts[-1]
    

if __name__ == '__main__':
    print(palindrome_partitioning_min_cuts("noonabbad"))
