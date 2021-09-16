def valid_ip_address(string):
    result = []
    for i in range(1, min(len(string), 4)):
        current = [""] * 4
        current[0] = string[:i]
        if not is_valid_ip_part(current[0]):
            continue
        for j in range(i + 1, i + min(len(string) - i, 4)):
            current[1] = string[i:j]
            if not is_valid_ip_part(current[1]):
                continue
            for k in range(j + 1, j + min(len(string) - j, 4)):
                current[2] = string[j:k]
                current[3] = string[k:]
                if is_valid_ip_part(current[2]) and is_valid_ip_part(current[3]):
                    result.append('.'.join(current))
    return result


def is_valid_ip_part(string):
    string_as_int = int(string)
    if string_as_int > 255:
        return False
    return len(string) == len(str(string_as_int))

print(valid_ip_address("1921680"))
# valid_ip_address("3700100")
