def powerset1(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i]+[element])
    return subsets

def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    element = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [element])
    
    return subsets


    
        




if __name__ == '__main__':
    array = [1, 2, 3]
    print(powerset(array))
