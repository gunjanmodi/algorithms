def remove_element(arr, key):
    j = 1
    for i in range(len(arr)):
        if arr[i] == key:
            arr[i] = arr[j]
            j += 1
    return j - 1    


if __name__ == '__main__':

    remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)