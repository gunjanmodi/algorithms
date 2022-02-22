def firstDuplicateValue(array):
    previous_idx = 0
    second_previous_idx = 0
    current_idx = 1
    while current_idx < len(array):
        current = array[current_idx]
        previous = array[previous_idx]
        if array[current_idx] == array[second_previous_idx]:
            return array[current_idx]
        if current < previous:
            array[current_idx], array[previous_idx] = array[previous_idx], array[current_idx]

        second_previous_idx = previous_idx
        previous_idx = current_idx
        current_idx += 1
    return -1


def first_duplicate_value(array):
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1


if __name__ == '__main__':
    # firstDuplicateValue([3, 1, 3, 1, 1, 4, 4])
    first_duplicate_value([3, 1, 3, 1, 1, 4, 4])
