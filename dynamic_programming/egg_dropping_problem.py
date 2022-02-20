"""
How to find base condition? smallest valid input
How to find memoization matrix dimension? variable that changes
"""

def egg_dropping(e, f):
    t = []
    for i in range(e + 1):
        t.append([-1 for _ in range(f + 1)])
    return solve(e, f, t)


def solve(e, f, t):
    if f == 0 or f == 1:
        return f
    if e == 1:
        return f

    if t[e][f] != -1:
        return t[e][f]

    min_answer = float('inf')
    for k in range(1, f + 1):
        temp_answer = 1 + max(solve(e - 1, k - 1, t), solve(e, f - k, t))
        min_answer = min(min_answer, temp_answer)
        t[e][f] = min_answer
    return min_answer


if __name__ == '__main__':
    print(egg_dropping(2, 10))
