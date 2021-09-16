def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = [num for num in array]

    max_sum_index = 0
    for i in range(len(array)):
        current_num = array[i]
        for j in range(0, i):
            other_num = array[j]
            if other_num < current_num and sums[j] + current_num >= sums[i]:
                sums[i] = sums[j] + current_num
                sequences[i] = j

        if sums[i] >= sums[max_sum_index]:
            max_sum_index = i

    return [sums[max_sum_index], build_sequence(array, sequences, max_sum_index)]
            

def max_sum_increasing_sub_sequence(array):

    sequences = [None for x in array]
    sums = [element for element in array]

    max_index = 0

    for i in range(0, len(array)):
        current = array[i]
        for j in range(0, i):
            other = array[j]
            if other < current and sums[j] + other >= sums[i]:
                sums[i] = sums[j] + other
                sequences[i] = j

            if sums[i] >= sums[max_index]:
                max_index = i


    return [sums[max_index], build_sequence(array, sequences, max_index)]





def build_sequence(array, sequences, current_index):
    sequence = []
    while current_index is not None:
        sequence.append(array[current_index])
        current_index = sequences[current_index]
    return list(reversed(sequence))

if __name__ == '__main__':
    print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
