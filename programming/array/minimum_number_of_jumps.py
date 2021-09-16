def min_jumps(arr):
    jump_count = 0
    i = 0
    while i < len(arr) - 1:
        jump_value = arr[i]
        i += jump_value
        jump_count += 1
    return jump_count


print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(min_jumps([1, 4, 3, 2, 6, 7]))