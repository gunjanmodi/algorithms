def main(string):
    i = 0 
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__ == '__main__':
    string = "abccpa"
    print(main(string))


# O(1) < O(log N) < O(n) < O(n2) < O(n3)



