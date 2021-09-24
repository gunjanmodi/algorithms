'''
AND
---------------
TT T
TF F
FT F
FF F

OR
----------------
TT T
TF T
FT T
FF F

XOR
----------------
TT F
TF T
FT T
FF F
'''


def count_ways(string):
    mp = {}
    return count_ways_helper(string, 0, len(string) - 1, True, mp)


def count_ways_helper(string, i, j, is_true, mp):
    if i > j:
        return 0
    if i == j:
        if is_true:
            return string[i] == 'T'
        else:
            return string[i] == 'F'

    key = f"{i}_{j}_{'t' if is_true else 'f'}"
    if key in mp:
        return mp[key]

    answer = 0
    k = i + 1
    while k <= j - 1:
        left_true = count_ways_helper(string, i, k - 1, True, mp)
        left_false = count_ways_helper(string, i, k - 1, False, mp)
        right_true = count_ways_helper(string, k + 1, j, True, mp)
        right_false = count_ways_helper(string, k + 1, j, False, mp)

        if string[k] == '&':
            if is_true:
                answer = answer + left_true * right_true
            else:
                answer = answer + left_true * right_false + left_false * right_true + left_false * right_false

        elif string[k] == '|':
            if is_true:
                answer = answer + left_true * right_true + left_true * right_false + left_false * right_true
            else:
                answer = answer + left_false * right_false

        elif string[k] == '^':
            if is_true:
                answer = answer + left_true * right_false + left_false * right_true
            else:
                answer = answer + left_true * right_true + left_false * right_false
        k += 2
    mp[key] = answer
    return answer


if __name__ == '__main__':
    print(count_ways("T|T&F^T"))
    print(count_ways("T^F|F"))
