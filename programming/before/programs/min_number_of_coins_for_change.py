def minNumberOfCoinsForChange1(n, denoms):
    denoms.sort(reverse=True)
    n_ref = n
    min_coins = {}
    for denom in denoms:
        if denom <= n:
            division = n // denom
            min_coins[denom] = division
            n -= denom * division
        

    total_coins = 0
    total = 0
    for k, v in min_coins.items():
        total_coins += v
        total += k * v
    if total != n_ref:
        return -1
    return total_coins


def minNumberOfCoinsForChange(n, denoms):
    nums = [float('inf') for amount in range(n+1)]
    nums[0] = 0
    for denom in denoms:
        for amount in range(len(nums)):
            if denom <= amount:
                nums[amount] = min(nums[amount], 1+ nums[amount - denom])

    return nums[n] if nums[n] != float("inf") else -1
    



if __name__ == '__main__':
    print(minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]))