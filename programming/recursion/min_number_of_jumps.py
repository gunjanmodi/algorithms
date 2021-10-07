def min_jumps(array):
    return solve(array, 0)


def solve(array, i):
    if i >= len(array) - 1:
        return 0
    if array[i] == 0:
        return float('inf')

    min_answer = float('inf')
    for j in range(i, i + array[i]):
        answer = 1 + solve(array, j + 1)
        min_answer = min(min_answer, answer)
    return min_answer


if __name__ == '__main__':
    print(min_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
    print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
    print(min_jumps([1, 4, 3, 2, 6, 7]))
