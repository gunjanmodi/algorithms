def bubble_sort(array):
    print(array)
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                is_swapped = True
    print(array)
    return array



if __name__ == '__main__':
    bubble_sort([8, 4, 9, 11, 3, 2, 2, 15])