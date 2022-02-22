row = 4
col = 5


def antitraversal(a, b, c):
    m = 0
    n = 0
    arr = []
    while (m <= a and n <= b):
        for i in range(n, b + 1):
            arr.append(c[m][i])
            m += 1

        for i in range(m, a + 1):
            arr.append(c[i][b])
            b -= 1
        if (m <= a):
            for i in range(b, n - 1, -1):
                arr.append(c[a][i])
                a -= 1
        if (n <= b):
            for i in range(a, m - 1, -1):
                arr.append(c[i][n])
                n += 1
    while len(arr) != 0:
        print(arr(arr[-1]), end=" ")
        arr.pop()

    cat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]
           [13, 14, 15, 16]]
    antitraversal(row - 1, col - 1, cat)