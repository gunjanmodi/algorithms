def run_length_encoding(string):
    if string == "" or None:
        return ""
    result = []
    count = 1
    prev_char = string[0]
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            count = 1
        prev_char = string[i]
    result.append(f"{count}{prev_char}")
    return "".join(result)


if __name__ == '__main__':
    print(run_length_encoding("aabcc"))
