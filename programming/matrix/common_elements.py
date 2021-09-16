def common_elements(matrix):
    reference = {}
    for i, row in enumerate(matrix):
        for value in row:
            if value in reference:
                reference[value]['count'] += 1
                reference[value]['rows'].add(i)
            else:
                reference[value] = {'count': 0, 'rows': set()}
                reference[value]['count'] += 1
                reference[value]['rows'].add(i)

    result = []
    for key, value in reference.items():
        all_rows_present = False
        if value['count'] >= len(matrix) - 1:
            all_rows_present = True
            for i in range(len(matrix)):
                if i not in value['rows']:
                    all_rows_present = False
        if all_rows_present:
            result.append(key)
    return result








print(common_elements([[1, 2, 1, 4, 8], [3, 7, 8, 5, 1], [8, 7, 7, 3, 1], [8, 1, 2, 7, 9]]))