def maxSubsetSumNoAdjacent1(array):
    ref_dict = {
        'non_adjacent_elements': [],
        'indexes_1': [],
        'indexes_2': []
    }
    for index, value in enumerate(array):
        if value in ref_dict['non_adjacent_elements']:
            ref_dict['indexes_1'].append(index)
            ref_dict['indexes_2'].append(index)
        if not (index - 1) in ref_dict['indexes_1'] and not (index - 1) in ref_dict['indexes_2']:
            ref_dict['non_adjacent_elements'].append(value)
            ref_dict['indexes_1'].append(index)
    return sum(ref_dict['non_adjacent_elements'])

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    max_sums = array[:]

    for i in range(0, len(array)):
        max_sums[i] = max(array[i-1], array[i] + array[i-2])
    return max_sums[-1]
    


if __name__ == '__main__':
    maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])