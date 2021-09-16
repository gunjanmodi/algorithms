def zigzag_convert(string, num_rows):
    if num_rows == 1:
        return string
    num_columns = (len(string) // num_rows) + num_rows
    matrix = [['-' for _col in range(num_columns)] for _row in range(num_rows)]
    if (num_rows * num_columns) < len(string):
        return string
    column_count, row_count = 0, 0
    string_iterator = 0

    while string_iterator < len(string):
        if column_count % (num_rows - 1) != 0:
            if (row_count + column_count) % (num_rows - 1) == 0:
                matrix[row_count][column_count] = string[string_iterator]
                string_iterator += 1
                row_count += 1
            else:
                row_count += 1
                if row_count == num_rows:
                    row_count = 0
                    column_count += 1
        else:
            if row_count < num_rows:
                matrix[row_count][column_count] = string[string_iterator]
                string_iterator += 1
                row_count += 1
            elif row_count == num_rows:
                row_count = 0
                column_count += 1

    result = []
    for row in matrix:
        for value in row:
            if value != '-':
                result.append(value)
    return "".join(result)


# output = zigzag_convert("PAYPALISHIRING", 1)
# print(output)
# output = zigzag_convert("PAYPALISHIRING", 2)
# print(output)
# output = zigzag_convert("PAYPALISHIRING", 3)
# print(output)
# output = zigzag_convert("PAYPALISHIRING", 4)
# print(output)
output = zigzag_convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 3)
print(output)