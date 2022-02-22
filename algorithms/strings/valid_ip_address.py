def valid_ip_iterative(string):
    result = []
    for i in range(3):
        first = string[:i + 1]
        if is_valid_part(first):
            for j in range(i + 1, i + 4):
                second = string[i + 1:j + 1]
                if is_valid_part(second):
                    for k in range(j + 1, j + 4):
                        third = string[j + 1:k + 1]
                        fourth = string[k + 1:]
                        if is_valid_part(third) and is_valid_part(fourth):
                            result.append(f'{first}.{second}.{third}.{fourth}')
    return result


def valid_ip_addresses_backtrack(string):
    result = []
    backtrack(string, "", 0, result)
    return result


def backtrack(string, temp_string, count, result):
    if count == 4 and not string:
        result.append(temp_string[:-1])
        return
    
    for i in range(1, 4):
        if i > len(string):
            return
        current = string[:i]
        if is_valid_part(current):
            backtrack(string[i:], temp_string+current+'.', count + 1, result)


def is_valid_part(string):
    if string and 0 <= int(string) <= 255 and len(string) == len(str(int(string))):
        return True
    return False


print(valid_ip_addresses_backtrack("25525511135"))
print(valid_ip_addresses_backtrack("0000"))
print(valid_ip_addresses_backtrack("1111"))