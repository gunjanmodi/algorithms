def subset_sum(array, total):
    n = len(array)
    t = []
    for i in range(n + 1):
        t.append([False for _ in range(total + 1)])

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n+1):
        for j in range(1, total+1):
            if array[i-1] <= j:
                t[i][j] = t[i-1][j-array[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    
    return t[n][total]


print(subset_sum([3, 34, 4, 12, 5, 2], 9))
print(subset_sum([3, 34, 4, 12, 5, 2], 30))