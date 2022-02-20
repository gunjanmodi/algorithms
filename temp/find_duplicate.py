def find_dups(nums):
    n = len(nums)
    for i in range(1, n):
        count1 = None
        count2 = None
        for num in nums:
            if count1 is None and num - i == 0:
                count1 = num
            elif count1 and num - i == 0:
                count2 = num
        # print(count1, count2, i)
        if count1 == count2 == i:
            return i





if __name__ == '__main__':
    print(find_dups([1, 3, 4, 2, 2]))
    print(find_dups([3,1,3,4,2]))
    print(find_dups([1, 1]))
    print(find_dups([1, 1, 2]))
