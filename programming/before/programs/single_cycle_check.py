def has_single_cycle(array):
    count_ref = [False for item in array]

    for i, value in enumerate(array):
        item = value
        
        if value < 0:
            item = value + i
        if item > len(array):
            item = len(array) - (value+1)


        count_ref[item] = True
    
    return count_ref[0]
    




if __name__ == '__main__':
#    has_single_cycle([2, 3, 1, -4, -4, 2])
   has_single_cycle([2, 2, -1]) 