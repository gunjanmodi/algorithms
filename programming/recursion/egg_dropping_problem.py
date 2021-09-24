def egg_dropping(e, f):
    return solve(e, f)


def solve(e, f):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f
    min_answer = float('inf')
    for k in range(1, f + 1):
        temp_answer = 1 + max(solve(e - 1, k - 1), solve(e, f - k))
        min_answer = min(min_answer, temp_answer)
    return min_answer


if __name__ == '__main__':
    print(egg_dropping(2, 10))
