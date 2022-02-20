def main(array, target):
    t = []
    n = len(array)
    for i in range(n + 1):
        t.append([0 for _ in range(target + 1)])
    
    for i in range(n + 1):
        t[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if array[i - 1] <= j:
                t[i][j] = t[i-1][j-array[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[-1][-1]
    
    

print(main([2,3,5,8,9,10], 10))
print(main([1, 2, 3, 4, 5], 10))
