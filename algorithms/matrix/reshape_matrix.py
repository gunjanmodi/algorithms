def reshape_matrix(mat, r, c):
        row = len(mat)
        column = len(mat[0])
        matrix_members = row * column

        if r * c > matrix_members and c >= column:
            c = column

        if matrix_members != r * c:
            return mat

        result = [[] for i in range(r)]
        row_count, column_count = 0, 0
        mat_row, mat_col = 0, 0
        main_count = 0
        while main_count < matrix_members:
            if column_count < c:
                value = mat[mat_row][mat_col]
                result[row_count].append(value)
                column_count += 1
                mat_col += 1
                if mat_col > len(mat[mat_row]) - 1:
                    mat_col = 0
                    mat_row += 1
                main_count += 1
            else:
                row_count += 1
                column_count = 0
        return result


# result1 = reshape_matrix([[1, 2], [3, 4]], 1, 4)
# print(result1)
# result2 = reshape_matrix([[1, 2],[3, 4]], 2, 4)
# print(result2)
result3 = reshape_matrix([[1, 2]], 1, 1)
print(result3)




