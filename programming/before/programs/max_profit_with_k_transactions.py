def max_profit_with_k_transactions(prices, k):
    profits = []
    for i in range(0, k+1):
        profits.append([0 for x in prices])
    
    for t in range(1, k+1):
        max_so_far = float('-inf')
        for d in range(len(prices)):
            max_so_far = max(max_so_far, profits[t - 1][d - 1] - prices[d-1])
            profits[t][d] = max(profits[t][d-1], prices[d] + max_so_far)
    
    return profits[-1][-1]

        
    
    # for p in profits:
        # print(p)

if __name__ == '__main__':
    max_profit_with_k_transactions([3, 2, 5, 7, 1, 3, 7], 2)