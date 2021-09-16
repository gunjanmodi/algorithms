# from itertools import permutations
#
#
# def all_permutations(string):
#     for perm in permutations(string):
#         print(perm)

def all_permutations(string):
    chars = [char for char in string]
    permutations = []
    permutation_helper(chars, [], permutations)
    return permutations


def permutation_helper(chars, current_permutation, permutations):
    if not len(chars) and len(current_permutation):
        permutations.append("".join(current_permutation))
    else:
        for i in range(len(chars)):
            new_chars = chars[:i]+chars[i+1:]
            new_permutation = current_permutation + [chars[i]]
            permutation_helper(new_chars,new_permutation, permutations)


# ABSG
# ABGS ABSG AGBS AGSB ASBG ASGB
# BAGS BASG BGAS BGSA BSAG BSGA
# SABG SAGB SBAG SBGA SGAB SGBA
# GABS GASB GBAS GBSA GSAB GSBA


print(all_permutations("ABSG"))
