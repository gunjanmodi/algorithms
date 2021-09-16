def insertion_sort(array):
    probe = 1
    for i in range(1, len(array)):
        for j in range(len(array[:probe])):
            if array[i] < array[j]:
                array[j], array[i] = array[i], array[j]
        probe += 1

    return array


        

if __name__ == '__main__':
    print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))