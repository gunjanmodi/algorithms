def min_insertions(string):
    string1 = string
    string2 = string[::-1]

    m = len(string1)
    n = len(string2) # Reversed string

    t = []
    for i in range(m + 1):
        t.append([0 for _ in range(n + 1)])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])

    return len(string) - t[-1][-1]


print(min_insertions("aebcbda"))