def max_profit(prices):
    k = 2
    if not len(prices):
        return 0
    profits = []
    for i in range(0, k + 1):
        profits.append([0 for x in prices])

    for t in range(1, k + 1):
        max_so_far = float('-inf')
        for d in range(1, len(prices)):
            max_so_far = max(max_so_far, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d - 1], prices[d] + max_so_far)

    return profits[-1][-1]


print(max_profit([10, 22, 5, 75, 65, 80]))
print(max_profit([3,2,6,5,0,3]))