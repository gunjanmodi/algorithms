def smallest_difference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    left = 0
    right = 0
    pair = [array_one[left], array_two[right]]
    smallest_diff = float("inf")
    current_diff = float("inf")

    while left < len(array_one) and right < len(array_two):
        if array_one[left] < array_two[right]:
            current_diff = array_two[right] - array_one[left]
            left += 1
        elif array_one[left] > array_two[right]:
            current_diff = array_one[left] - array_two[right]
            right += 1

        if current_diff < smallest_diff:
            smallest_diff = current_diff
            pair[0] = array_one[left]
            pair[1] = array_two[right]

    return pair


if __name__ == '__main__':

    output = smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    print(output)