def climb_stairs(n):
    memo = {}

    def helper(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]
    
    return helper(n)


print(climb_stairs(2))
print(climb_stairs(3))