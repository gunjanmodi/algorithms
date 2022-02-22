def reverse_words_in_string(string):
    broken_string = do_break(string)
    reverse_strings = do_reverse(broken_string)
    return " ".join(reverse_strings)


def do_break(string):
    broken_string = []
    current_word = []
    for character in string:
        if character == " ":
            broken_string.append("".join(current_word))
            current_word = []
        else:
            current_word.append(character)
    broken_string.append("".join(current_word))
    return broken_string


def do_reverse(str_array):
    result = []
    for i in reversed(range(len(str_array))):
        result.append(str_array[i])
    return result


output = reverse_words_in_string("AlgoExpert is the best!")
print(output)
# do_break_2("AlgoExpert is the best!")
