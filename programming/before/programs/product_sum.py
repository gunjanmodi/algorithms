def productSum(array, multiplier=1):
    sum = 0
    for value in array:
        if isinstance(value, list):
            sum += productSum(value, multiplier + 1)
        else:
            sum += value
    return sum * multiplier

if __name__ == '__main__':
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    print(productSum(array))