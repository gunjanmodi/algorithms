def max_product_subarray(array):
    current_max = array[0]
    current_min = array[0]
    answer = array[0]
    for i in range(1, len(array)):
        num = array[i]
        if num < 0:
            current_max, current_min = current_min, current_max
        current_max = max(num, num * current_max)
        current_min = min(num, num * current_min)

        answer = max(answer, current_max)
    return answer


print(max_product_subarray([6, -3, -10, 0, 2]))
print(max_product_subarray([2, 3, 4, 5, -1, 0]))
print(max_product_subarray([8, -2, -2, 0, 8, 0, -6, -8, -6, -1]))
