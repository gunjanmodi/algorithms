"""
Given a string, find the length of the longest substring, which has no repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
"""

def non_repeat_substring(string):
    last_seen = {}
    window_start = 0
    longest = [0, 0]
    for window_end in range(len(string)):
        char = string[window_end]
        if char in last_seen:
            window_start = max(window_start, last_seen[char] + 1)
        last_seen[char] = window_end
        if longest[1] - longest[0] < window_end +1 - window_start:
            longest = [window_start, window_end + 1]
    return string[longest[0]:longest[1]]

    




if __name__ == '__main__':
    output = non_repeat_substring("aabccbb")
    print(output)