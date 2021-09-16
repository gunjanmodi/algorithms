def bubbleSort(array):
    swap_occured = False
    for i in range(len(array)):
        if i+1 < len(array) and array[i+1] < array[i]:
            array[i], array[i+1] = array[i+1], array[i]
            swap_occured = True
    
    if swap_occured:
        bubbleSort(array)
    return array

if __name__ == '__main__':
    print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))