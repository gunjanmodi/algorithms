# def row_with_max1s(matrix):
#     max_row_count = 0
#     resulting_row = -1
#     for i in range(len(matrix)):
#         current_row_count = 0
#         for num in matrix[i]:
#             if num == 1:
#                 current_row_count += 1
#         if current_row_count > max_row_count:
#             resulting_row = i
#             max_row_count = current_row_count
#     return resulting_row

def find_first_one(array, left, right):
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or array[mid - 1] == 0 ) and array[mid] == 1:
            return mid
        elif array[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def row_with_max1s(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    answer = float('inf')
    answer_index = -1
    for i, row in enumerate(matrix):
        first_index = find_first_one(row, 0, cols - 1)
        if first_index != -1:
            if first_index < answer:
                answer =  first_index
                answer_index = i
    return answer_index



print(row_with_max1s([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
# print(row_with_max1s([[0, 0], [1, 1]]))
