def mcm(array):
    t = []
    for i in range(len(array)):
        t.append([-1 for _ in range(len(array))])
    return mcm_helper(array, 1, len(array) - 1, t)


def mcm_helper(array, i, j, t):
    if i >= j:
        return 0

    if t[i][j] != -1:
        return t[i][j]

    min_answer = float('inf')
    for k in range(i, j):
        temp_answer = mcm_helper(array, i, k, t) + mcm_helper(array, k + 1, j, t) + (array[i - 1] * array[k] * array[j])
        min_answer = min(min_answer, temp_answer)
        t[i][j] = min_answer
    return min_answer


if __name__ == '__main__':
    print(mcm([40, 20, 30, 10, 30]))