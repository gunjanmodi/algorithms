# def do_permutations(array):
#     permutations = []
#     permutation_helper(array, [], permutations)
#     return permutations

# def permutation_helper(array, current_permutation, permutations):
#     if not len(array) and len(current_permutation):
#         permutations.append(current_permutation)
#     else:
#         for i in range(len(array)):
#             new_array = array[:i] + array[i + 1:]
#             new_permutation = current_permutation + [array[i]]
#             permutation_helper(new_array, new_permutation, permutations)

def main():
    output = do_permutations([1,2,3])
    print(output)

main()



