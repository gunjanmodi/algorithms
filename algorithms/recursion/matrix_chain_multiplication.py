def mcm(array):
    return mcm_helper(array, 1, len(array) - 1)


def mcm_helper(array, i, j):
    if i >= j:
        return 0
    min_answer = float('inf')
    for k in range(i, j):
        temp_answer = mcm_helper(array, i, k) \
                      + mcm_helper(array, k + 1, j) \
                      + (array[i - 1] * array[k] * array[j])
        min_answer = min(min_answer, temp_answer)
    return min_answer


if __name__ == '__main__':
    print(mcm([40, 20, 30, 10, 30]))
