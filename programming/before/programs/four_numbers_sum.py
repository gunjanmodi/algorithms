def four_numbers_sum1(array, target):
    pairs = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            for k in range(j, len(array)):
                for l in range(k, len(array)):
                    if array[i] + array[j] + array[k] + array[l] == target and \
                    array[i] != array[j] != array[k] != array[l] :
                        pairs.append([array[i], array[j], array[k], array[l]])

    return pairs


def four_numbers_sum(array, target):
    quadruplets = []
    pairs_dict = {}
    
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            difference = target - current_sum
            if difference in pairs_dict:
                for pair in pairs_dict[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pairs_dict:
                pairs_dict[current_sum] = [ [ array[i], array[k]] ]
            else:
                pairs_dict[current_sum].append([ array[i], array[k] ])
    return quadruplets        


if __name__ == '__main__':
    four_numbers_sum([7, 6, 4, -1, 1, 2], 16)