def is_valid_subsequence1(array, sub_sequence):
    array_index = 0
    seq_index = 0
    while array_index <= len(array) - 1 and seq_index <= len(array) - 1:
        if array[array_index] == sub_sequence[seq_index]:
            seq_index += 1
        array_index += 1
    return seq_index == len(sub_sequence)

def is_valid_subsequence(array, sequence):
    seq_index = 0
    for item in array:
        if seq_index == len(sequence):
            break
        if item == sequence[seq_index]:
            seq_index += 1
    return seq_index == len(sequence)




if __name__ == '__main__':
    print(is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))