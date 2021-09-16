def fruits_into_basket(fruits):
    fruits_frequency = {}
    window_start = 0
    unique_chars = 0
    max_length = 0
    for window_end in range(len(fruits)):
        fruit = fruits[window_end]
        if not fruit in fruits_frequency:
            fruits_frequency[fruit] = 1
        else:
            fruits_frequency[fruit] += 1
        
        while len(fruits_frequency) > 2:
            left_fruit = fruits[window_start]
            fruits_frequency[left_fruit] -= 1
            if fruits_frequency[left_fruit] == 0:
                del fruits_frequency[left_fruit]
            window_start += 1
        max_length = max(max_length, window_end - window_start  + 1)
    return max_length


if __name__ == '__main__':
    output = fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C'])
    print(output)