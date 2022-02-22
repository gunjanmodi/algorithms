def sub_array_sum_zero(nums):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums,0)
        d[sums] = d.get(sums,0) + 1
    return True if count > 0 else False


if __name__ == '__main__':
    print(sub_array_sum_zero([4, 2, -3, 1, 6]))
    print(sub_array_sum_zero([10, -10]))





