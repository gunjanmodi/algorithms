def max_profit(prices):
    result = []
    n = len(prices)
    if n == 1:
        return result

    i = 0

    while i < n - 1:
        while i < n - 1 and prices[i + 1] <= prices[i]:
            i += 1

        if i == len(prices) - 1:
            break

        buy = i
        i += 1

        while i < n - 1 and prices[i - 1] <= prices[i]:
            i += 1

        sell = i - 1

        result.append([buy, sell])

    return result if len(result) > 0 else []



# print(max_profit([100, 180, 260, 310, 40, 535, 695]))
# print(max_profit([4, 2, 2, 2, 4]))
# print(max_profit([16, 21, 23, 80, 79, 30, 59, 41, 52, 8, 35]))
print(max_profit([10, 22, 5, 75, 65, 80]))