from collections import deque


def check_mirror_tree(e, A, B):
    n = len(A)
    array_a = []
    array_b = []

    for i in range(n):
        array_a.append(deque())
        array_b.append(deque())

    for i in range(0, 2 * e, 2):
        array_a[A[i]].append(A[i + 1])
        array_b[B[i]].append(B[i + 1])

    for i in range(1, n):
        while len(array_a[i]) > 0 and len(array_b[i]) > 0:
            if array_a[i].popleft() != array_b[i].pop():
                return 0
    return 1


print(check_mirror_tree(2, [1, 2, 1, 3], [1, 3, 1, 2]))
print(check_mirror_tree(2, [1, 2, 1, 3], [1, 2, 1, 3]))