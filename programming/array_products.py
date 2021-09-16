def array_of_products(array):
    products = [1 for _ in range(len(array))]

    left_multiplication = 1
    for i in range(len(array)):
        products[i] = left_multiplication
        left_multiplication *= array[i]

    right_multiplication = 1
    for i in reversed(range(len(array))):
        products[i] *= right_multiplication
        right_multiplication *= array[i]
    return products


if __name__ == '__main__':
    result = array_of_products([5, 1, 4, 2])
    print(result)
