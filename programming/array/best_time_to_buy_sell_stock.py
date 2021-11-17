def max_profit(prices):
    if not prices:
        return 0

    min_purchase = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_purchase)
        min_purchase = min(min_purchase, prices[i])
    return max_profit

if __name__ == '__main__':
    print(max_profit([3,2,6,5,0,3])) # Expected 4
    print(max_profit([2,1,2,1,0,1,2])) # Expected 2
    print(max_profit([7,1,5,3,6,4]))
    print(max_profit([7,6,4,3,1]))