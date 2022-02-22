def word_break(line, dictionary):
    dictionary = set(dictionary)

    current_word = ""
    answer = 0
    for character in line:
        current_word += character
        if character in dictionary:
            current_word = ""
            answer = 1
    return answer


# print(word_break("ilikesamsung", ["i", "like", "sam",
#                             "sung", "samsung", "mobile",
#                             "ice","cream", "icecream",
#                             "man", "go", "mango"]))

print(word_break("lrbbmqbabowkkab", ["lrbbmqb", "cd", "r", "owkk"], ))
