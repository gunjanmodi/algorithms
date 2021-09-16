def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))
    return ''.join(new_letters)


def get_new_letter(letter, key, alphabet):
    new_index = alphabet.index(letter) + key
    return alphabet[new_index] if new_index <= 25 else alphabet[-1 + new_index % 25]
    

def caesar_cipher_encryptor1(string, key):
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letters.append(get_new_letter1(letter, new_key))
    return ''.join(new_letters)

def get_new_letter1(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)

if __name__ == '__main__':
    print(caesar_cipher_encryptor("xyz", 2))