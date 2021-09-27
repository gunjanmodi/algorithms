def main(array):
    n = len(array)
    t = [1 for _ in range(n)]
    max_so_far = 1

    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                t[i] = max(t[i], 1 + t[j])
                max_so_far = max(max_so_far, t[i])
    return max_so_far


if __name__ == '__main__':
    print(main([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
