def sub_array_exists(arr):
    # window_size = 0
    # while window_size < len(arr):
    #     window_start = 0
    #     window_sum = arr[window_start]
    #     for window_end in range(window_start+1, len(arr)):
    #         window_sum += arr[window_end]
    #
    #         if window_end > window_size:
    #             window_sum -= arr[window_start]
    #             window_start += 1
    #
    #         if window_sum == 0:
    #             return True
    #     window_size += 1
    #
    # return False

    # create a python dict
    hashMap = {}
    n = len(arr)
    # create a python list
    # equivalent to ArrayList
    out = []

    # tracker for sum of elements
    sum1 = 0
    for i in range(n):

        # increment sum by element of array
        sum1 += arr[i]

        # if sum is 0, we found a subarray starting
        # from index 0 and ending at index i
        if sum1 == 0:
            out.append((0, i))
        al = []

        # If sum already exists in the map
        # there exists at-least one subarray
        # ending at index i with 0 sum
        if sum1 in hashMap:

            # map[sum] stores starting index
            # of all subarrays
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    return out

print(sub_array_exists([4, 2, -3, 0, 1, 6]))
print(sub_array_exists([10, -10]))





