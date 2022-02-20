def choin_change_number_of_ways(coins, amount):
    n = len(coins)
    t = []

    for i in range(n + 1):
        t.append([-1 for _ in range(amount + 1)])

    for i in range(n + 1):
        for j in range(amount + 1):
            if i == 0:
                t[i][j] = 0

            if j == 0:
                t[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i][j - coins[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[-1][-1]


if __name__ == '__main__':
    print(choin_change_number_of_ways([1, 2, 3], 4))
    print(choin_change_number_of_ways([2, 5, 3, 6], 4))
