def recursive_dp(values, weights, w):
    n = len(weights)
    t = []
    for i in range(n + 1):
        t.append([-1 for _ in range(w + 1)])
    
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                t[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if weights[i - 1] <= j:
                t[i][j] = max(t[i-1][j], values[i - 1] + t[i][j-weights[i-1]])
            else:
                t[i][j] = t[i-1][j]
    return t[-1][-1]


def knapsack_recursive(values,weights, w, n, t):
    if w == 0 or n == 0:
        return 0
    if t[n][w] == -1:
        if weights[n] <= w:
            return max(
                values[n] + knapsack_recursive(values, weights, w-weights[n], n, t),
                knapsack_recursive(values, weights, w, n - 1, t)
            )
        else:
            return knapsack_recursive(values, weights, w, n - 1, t)
    return t[n][w]

print(recursive_dp([1, 30], [1, 50], 100))
