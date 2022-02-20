def find_missing_number(arr):
    x1 = 1
    for i in range(2, len(arr)+2):
        x1 = x1 ^ i

    x2 = arr[0]
    for i in range(1, len(arr)):
        x2 = x2 ^ arr[i]
    print(x1)
    print(x2)
    return x1 ^ x2

def main():
    arr = [1, 5, 2, 6, 4] 
    print('Missing number is:' + str(find_missing_number(arr)))

main()

    