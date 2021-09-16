def longest_substring_with_k_distinct(string, k):
    window_start = 0
    num_of_distinct_chars = 0
    char_frequency = {}
    max_length = 0
    for window_end in range(len(string)):
        current = string[window_end]
        if current not in char_frequency:
            char_frequency[current] = 1
            num_of_distinct_chars += 1
        else:
            char_frequency[current] += 1

        if num_of_distinct_chars > k:
            window_start += 1
            num_of_distinct_chars -= 1

        window_length = window_end - window_start  + 1
        max_length = max(max_length, window_length)
    return max_length


if __name__ == '__main__':
    output = longest_substring_with_k_distinct("araaci", 2)
    print(output)