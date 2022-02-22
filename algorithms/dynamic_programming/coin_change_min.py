def main(coins, amount):
    n = len(coins)
    t = []

    for i in range(n + 1):
        t.append([-1 for _ in range(amount + 1)])

    for i in range(n + 1):
        for j in range(amount + 1):
            if j == 0:
                t[i][0] = 0
            if i == 0:
                t[0][j] = float('inf')

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                t[i][j] = min(t[i - 1][j], 1 + t[i][j - coins[i - 1]])
            else:
                t[i][j] = t[i - 1][j]

    return t[-1][-1]


if __name__ == '__main__':
    print(main([3, 4, 5], 5))
    print(main([1, 2, 3], 5))