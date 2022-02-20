def find_target_sum_ways(nums, target):
    current_sum = 0
    n = len(nums) - 1
    memo = {}
    
    def solve(nums, target, current_sum, n):
        key = (n, current_sum)
        
        if key in memo:
            return memo[key]
        
        
        if n < 0 and current_sum == target:
            return 1
        
        if n < 0:
            return 0
        
        positive = solve(nums, target, current_sum + nums[n], n - 1)
        negative = solve(nums, target, current_sum - nums[n], n - 1)
        
        memo[key] = positive + negative
        return memo[key]

    return solve(nums, target, current_sum, n)

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    find_target_sum_ways()