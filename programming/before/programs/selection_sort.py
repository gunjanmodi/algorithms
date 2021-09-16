def selection_sort(array):
    current_index = 0
    while current_index < len(array) - 1:
        minimum = current_index
        for i in range(current_index + 1, len(array)):
            if array[i] < array[minimum]:
                minimum = i
        array[current_index], array[minimum] = array[minimum], array[current_index]
        current_index += 1
    return array

if __name__ == '__main__':
    print(selection_sort([8, 5, 2, 9, 5, 6, 3]))