def getPermutations1(array):
    permutations = []
    permutations_helper1(array, [], permutations)
    return permutations

def permutations_helper1(array, current_permutation, permutations):
    if not len(array) and len(current_permutation):
        permutations.append(current_permutation)

    for i in range(len(array)):
        new_array = array[:i] + array[i + 1 :]
        current_permutation = current_permutation + [array[i]]
        permutations_helper1(new_array, current_permutation, permutations)

def getPermutations(array):
    permutations = []
    permutations_helper(0, array, permutations)

def permutations_helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    for j in range(i, len(array)):
        swap(array, i, j)
        permutations_helper(i+1, array, permutations)
        swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

if __name__ == '__main__':
    # getPermutations1([1, 2, 3])
    getPermutations([1, 2, 3])