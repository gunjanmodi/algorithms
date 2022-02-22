def sorted_squared_array(array):
    sorted_squares = [0 for _ in array]
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_squares[idx] = smaller_value * smaller_value
            smaller_value_idx += 1
        else:
            sorted_squares[idx] = larger_value * larger_value
            larger_value_idx -= 1
    print(sorted_squares)
    return sorted_squares

if __name__ == '__main__':
    sorted_squared_array([-3, -2, -1, 0, 1, 2, 3])