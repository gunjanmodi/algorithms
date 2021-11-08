def sub_array_exists(nums, k):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums-k,0)
        d[sums] = d.get(sums,0) + 1
    return True if count > 0 else False


if __name__ == '__main__':
    print(sub_array_exists([1, 1, 1], 2))
    print(sub_array_exists([1,2,3], 3))





