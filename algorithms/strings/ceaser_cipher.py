def ceaser_cipher_encrypter(string, key):
    result = []
    all_characters = "abcdefghijklmnopqrstuvwxyz"
    reference = {}
    reverse_reference = {}
    counter = 0
    for letter in all_characters:
        order = 97 + counter
        reference[letter] = order
        reverse_reference[order] = letter
        counter += 1

    for character in string:
        order = reference[character]
        new_order = order + key
        if new_order > 122:
            new_order -= 26
        new_character = reverse_reference[new_order]
        result.append(new_character)
    return "".join(result)


output = ceaser_cipher_encrypter("xyz", 2)
print(output)
