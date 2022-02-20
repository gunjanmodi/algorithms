def lps(string):
    string1 = string
    j = len(string) - 1
    temp = []
    while j >= 0:
        temp.append(string[j])
        j -= 1

    string2 = ''.join(temp)

    m = len(string1)
    n = len(string2)
    t = []
    for i in range(m + 1):
        t.append([0 for _ in range(n + 1)])

    max_so_far = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = 0
            max_so_far = max(max_so_far, t[i][j])
    return max_so_far


if __name__ == '__main__':
    print(lps("aaaabbaa"))
    # print(lps("abcd"))
    # print(lps("aba"))
