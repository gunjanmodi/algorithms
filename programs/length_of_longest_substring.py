def length_of_longest_substring(string, k):
    char_frequency = {}
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0

    for window_end in range(len(string)):
        char = string[window_end]
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, char_frequency[char])

        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = string[window_start]
            char_frequency[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':

    length_of_longest_substring("aabccbb", 2)