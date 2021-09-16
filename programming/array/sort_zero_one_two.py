def sort012(arr,n):
    count_zero, count_one, count_two = 0, 0, 0
    for num in arr:
        if num == 0:
            count_zero += 1
        elif num == 1:
            count_one += 1
        elif num == 2:
            count_two += 1

    i = 0
    while i < len(arr):
        while count_zero > 0:
            arr[i] = 0
            count_zero -= 1
            i += 1

        while count_one > 0:
            arr[i] = 1
            count_one -= 1
            i += 1

        while count_two > 0:
            arr[i] = 2
            count_two -= 1
            i += 1
    return arr


def dutch_national_flag(array):
    red = 0
    white = 0
    blue = len(array) - 1
    while white <= blue:
        if array[white] == 0:
            array[red], array[white] = array[white], array[red]
            red += 1
            white += 1
        elif array[white] == 1:
            white += 1
        elif array[white] == 2:
            array[white], array[blue] = array[blue], array[white]
            blue -= 1
    return array


print(dutch_national_flag([0, 2, 1, 2, 0]))
print(sort012([0, 2, 1, 2, 0], 5))