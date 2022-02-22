def cut_rod(prices, n):
    lengths = [i for i in range(1, n+1)]
    t = []
    for i in range(n + 1):
        t.append([0 for i in range(n + 1)])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if lengths[i - 1] <= j:
                t[i][j] = max(
                    prices[i  - 1] + t[i][j - lengths[i - 1]],
                    t[i - 1][j]
                )
            else:
                t[i][j] = t[i - 1][j]

    return t[-1][-1]


print(cut_rod([1, 5, 8, 9, 10, 17, 17, 20], 8))