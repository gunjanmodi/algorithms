def roman_to_int(roman):
    symbols = {
        'I': {'value': 1, 'largers': {'V', 'X', 'L', 'C', 'D', 'M'}},
        'V': {'value': 5, 'largers': {'X', 'L', 'C', 'D', 'M'}},
        'X': {'value': 10, 'largers': {'L', 'C', 'D', 'M'}},
        'L': {'value': 50, 'largers': {'C', 'D', 'M'}},
        'C': {'value': 100, 'largers': {'D', 'M'}},
        'D': {'value': 500, 'largers': {'M'}},
        'M': {'value': 1000, 'largers': {}},
    }

    str_array = [char for char in roman]
    integer = 0
    char = 0
    while char < len(str_array):
        symbol = str_array[char]
        if char == len(str_array) - 1:
            integer += symbols[symbol]['value']
            char += 1
        else:
            if str_array[char + 1] in symbols[symbol]['largers']:
                current_symbol_value = symbols[symbol]['value']
                next_symbol_value = symbols[str_array[char + 1]]['value']
                integer = integer + next_symbol_value - current_symbol_value
                char += 2
            else:
                integer += symbols[symbol]['value']
                char += 1
    return integer



# print(roman_to_int('III'))
# print(roman_to_int('IV'))
# print(roman_to_int('IX'))
# print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))




