"""
Clarification (~2 min)
Start with the naive solution (~3 min)
Optimize the naive solution (~10 min)
Translate the pseudocode into real code (~15 min)
Test thoroughly (5 min)
Analyze time and space complexity (1 min)
"""


# Time: O() | Space: O()
def main(phone_number):
    digits_mapping = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    result = []
    array = []
    phone_number_mnemonics_helper(phone_number, 0, array, digits_mapping, result)
    return result


def phone_number_mnemonics_helper(phone_number, k, array, digits_mapping, result):
    if k == len(phone_number):
        result.append(''.join(array[:]))
        return
    current_mapping = digits_mapping.get(phone_number[k], phone_number[k])
    for letter in current_mapping:
        array.append(letter)
        phone_number_mnemonics_helper(phone_number, k + 1, array, digits_mapping, result)
        array.pop()



# Test cases: Normal1, Normal2, Normal3, Negative, Empty, Too long
print(main("23"))
print(main(""))
print(main("2"))
print(main("1905"))
print(main("234"))
print(main("982"))